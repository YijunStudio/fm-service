FROM python:3.7
WORKDIR /

ENV TZ=Asia/Shanghai
RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN --mount=type=secret,id=APPID export APPID=$(cat /run/secrets/APPID)

RUN echo $APPID  && \
    echo $APPSECRET && \
    echo $DB_HOST && \
    echo $DB_PORT && \
    echo $DB_USER && \
    echo $DB_PASS && \
    echo $DB_NAME

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
# CMD [ "python", "app.py" ]