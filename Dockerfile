FROM python:3.7
WORKDIR /

ENV TZ=Asia/Shanghai
RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

# RUN --mount=type=secret,id=APPID export APPID=$(cat /run/secrets/APPID) && echo $APPID
# RUN --mount=type=secret,id=APPSECRET export APPSECRET=$(cat /run/secrets/APPSECRET)
# RUN --mount=type=secret,id=DB_HOST export DB_HOST=$(cat /run/secrets/DB_HOST)
# RUN --mount=type=secret,id=DB_PORT export DB_PORT=$(cat /run/secrets/DB_PORT) && echo $DB_PORT
# RUN --mount=type=secret,id=DB_USER export DB_USER=$(cat /run/secrets/DB_USER)
# RUN --mount=type=secret,id=DB_PASS export DB_PASS=$(cat /run/secrets/DB_PASS)
# RUN --mount=type=secret,id=DB_NAME export DB_NAME=$(cat /run/secrets/DB_NAME)

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
# CMD [ "python", "app.py" ]