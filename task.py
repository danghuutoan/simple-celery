from celery import Celery
from celery.signals import worker_process_init, celeryd_init
import os
import time

QUEUE_DOMAIN = os.getenv("QUEUE_DOMAIN", "localhost")
app = Celery('tasks', broker=f'pyamqp://guest@{QUEUE_DOMAIN}/')


# @celeryd_init.connect
# def configure_workers(sender=None, conf=None, **kwargs):
#     conf.worker_proc_alive_timeout = 30.0

@worker_process_init.connect
def process_init(**_):
	print("process init")
	time.sleep(6)

@app.task
def add(x, y):
    return x + y