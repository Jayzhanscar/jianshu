from celery import Celery, task

app = Celery('__name__', broker='redis://localhost:6379')

import requests
import json
import time
from mail import send_email

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']


HOST_IP = "127.0.0.1"

BROKER_URI = 'redis://%s:6379/6' % HOST_IP
BACKEND_URI = 'redis://%s:6379/5' % HOST_IP

worker = Celery('celery_worker', broker=BROKER_URI, backend=BACKEND_URI)


@app.task
def add():
    send()
    print('this is my task')


@worker.task
def send():
    content = '测试定时功能'
    send_email('959370553@qq.com,zhanljscarever@163.com', 'D:\\test', content)
    print('i has send the mail')


from celery.schedules import crontab

worker.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    beat_schedule={
        "morning_msg_1": {
            "task": "tasks.send",
            "schedule": crontab(minute=17, hour=0),
            "args": ("ok",)
        },
        "morning_msg_2": {
            "task": "tasks.send",
            "schedule": crontab(minute=18, hour=0),
            "args": ("ok",)
        }
    }
)

send()