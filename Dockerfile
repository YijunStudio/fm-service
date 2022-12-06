FROM python:3.7
WORKDIR /

ENV TZ=Asia/Shanghai
RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN --mount=type=secret,id=APPID \
    --mount=type=secret,id=APPSECRET \
    export APPID=$(cat /run/secrets/APPID) && \
    export APPSECRET=$(cat /run/secrets/APPSECRET) && \

RUN echo $APPID
RUN echo $APPSECRET
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
# CMD [ "python", "app.py" ]