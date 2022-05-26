from celery import Celery

# from celery.signals import worker_process_init, celeryd_init
import celeryconfig

app = Celery("tasks")
app.config_from_object(celeryconfig)


@app.task()
def add(x, y):
    return x + y
