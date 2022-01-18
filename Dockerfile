FROM python:3

RUN mkdir -p /usr/src/app

COPY requirements.txt ./
COPY start.sh /start.sh

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod -x /start.sh

WORKDIR /usr/src/app
COPY app /usr/src/app

CMD [ "bash", "/start.sh" ]
