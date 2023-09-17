FROM python:3.7.5-slim
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt    
RUN pip install -r requirements.txt
COPY . /app

CMD [ "python","./main.py" ]