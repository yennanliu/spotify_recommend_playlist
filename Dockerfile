
FROM python:3.6

EXPOSE 7777

WORKDIR  /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app
CMD python server.py