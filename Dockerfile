FROM python:3.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y && apt-get update -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN  apt-get install build-essential -y
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    libmariadbclient-dev


RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app/
ENV DATABASE_URL=mysql://root:example@db:3306/myflaskapp?charset=utf8mb4

EXPOSE 5000

CMD ["python3", "app.py"]
