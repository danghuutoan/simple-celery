from celery import Celery
from celery.signals import worker_process_init, celeryd_init
import os
import time

QUEUE_DOMAIN = os.getenv("QUEUE_DOMAIN", "localhost")
app = Celery("tasks", broker=f"amqp://guest@queue:5672/")


@celeryd_init.connect
def configure_workers(sender=None, conf=None, **kwargs):
    conf.worker_proc_alive_timeout = 30.0
    # conf.broker_heartbeat = 0
    conf.broker_connection_timeout = 300


@worker_process_init.connect
def process_init(**_):
    print("process init")
    time.sleep(6)


@app.task(acks_late=True)
def add(x, y):
    count = 0
    while count < 400:
        time.sleep(1)
        print(f"####{count}")
        count += 1
    return x + y
