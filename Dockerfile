FROM python:3.7.3-alpine

WORKDIR /usr/src/app

COPY main.py .

CMD [ "python3", "main.py" ]
