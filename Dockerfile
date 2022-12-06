FROM python:3.7
WORKDIR /

ENV TZ=Asia/Shanghai
RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN ls /run/secrets

RUN --mount=type=secret,id=APPID export APPID=$(cat /run/secrets/APPID)

RUN --mount=type=secret,id=APPID \
    export APPID=$(cat /run/secrets/APPID) && \
    --mount=type=secret,id=APPSECRET \
    export APPSECRET=$(cat /run/secrets/APPSECRET) && \
    --mount=type=secret,id=DB_HOST \
    export DB_HOST=$(cat /run/secrets/DB_HOST) && \
    --mount=type=secret,id=DB_PORT \
    export DB_PORT=$(cat /run/secrets/DB_PORT) && \
    --mount=type=secret,id=DB_USER \
    export DB_USER=$(cat /run/secrets/DB_USER) && \
    --mount=type=secret,id=DB_PASS \
    export DB_PASS=$(cat /run/secrets/DB_PASS) && \
    --mount=type=secret,id=DB_NAME \
    export DB_NAME=$(cat /run/secrets/DB_NAME) && \

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