FROM python:3.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y && apt-get update -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app/
EXPOSE 5000

CMD ["python3", "app.py"]

