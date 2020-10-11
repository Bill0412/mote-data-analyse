FROM python:3
LABEL maintainer="jxphxufh@gmail.com"
EXPOSE 5000/tcp

ENV API_HOST=127.0.0.1

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD python main.py --host $API_HOST

