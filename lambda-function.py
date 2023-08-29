import logging
import telegram
from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import Filters 
import requests
import os
import time
import json
from datetime import datetime

# Initialize the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token
BOT_TOKEN = 'bot-toke'

def start(update: telegram.Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me an image to remove the background!")

def process_image(update: telegram.Update, context: CallbackContext) -> None:
    try:
        # Get the photo file
        photo = update.message.photo[-1].get_file(timeout=None)

        # Download the photo
        input_path = "/tmp/input.jpg"
        output_path = "/tmp/output.png"

        photo.download(input_path)

        # Call Removal.BG API
        headers = {
            'X-Api-Key': 'api-key',
        }

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            headers=headers,
            files={'image_file': open(input_path, 'rb')},
            data={'size': 'auto'},
        )

        if response.status_code == requests.codes.ok:
            with open(output_path, 'wb') as out:
                out.write(response.content)
                efs_path = '/mnt/efs'
                now = datetime.now()
                file_name = now.strftime("%Y%m%d_%H%M%S.png")
                efs_file_path = os.path.join(efs_path, file_name)
                with open(output_path, 'rb') as f:
                    with open(efs_file_path, 'wb') as efs_f:
                        efs_f.write(f.read())
                        
                # Send the processed image back
                with open(output_path, "rb") as f:
                    update.message.reply_photo(photo=f)
        else:
            logger.error("Removal.BG API Error: %s", response.status_code)

    except Exception as e:
        logger.error("Error in process_image: %s", str(e))

def lambda_handler(event, context):
    try:
        # Create a Bot instance
        bot = telegram.Bot(token=BOT_TOKEN)
        
        # Create an Updater and pass it the Bot instance
        updater = Updater(bot=bot, use_context=True)
        dispatcher = updater.dispatcher

        # Add command and message handlers
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.photo, process_image))

        # Parse the incoming event from API Gateway
        update = telegram.Update.de_json(json.loads(event['body']), updater.bot)
        dispatcher.process_update(update)

        return {
            'statusCode': 200,
            'body': 'Message processed successfully'
        }

    except Exception as e:
        logger.error("Error in lambda_handler: %s", str(e))
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
