from celery import Celery
app = Celery(
    "task", broker="amqp://guest@localhost:5672//", backend='amqp://'
)
res = app.send_task(
        "task.add", bind=True, args=[4,4]
    )

print(res.get())
