from task import add
from celery import Celery
app = Celery(
    "task", broker="amqp://guest@192.168.1.2:5672//"
)

app.send_task(
        "task.add", bind=True, args=[4,4]
    )
# QUEUE_DOMAIN = os.getenv("QUEUE_DOMAIN", "localhost")
# app = Celery("tasks", broker=f"pyamqp://guest@{QUEUE_DOMAIN}/")

# # print(dir(app))

# with app.connection() as connection:
#     recv = app.events.Receiver(connection,)
#     recv.capture(limit=None, timeout=None, wakeup=True)

#     state = app.events.State()
#     # print(dir(state))
#     print(state.tasks_by_timestamp())
#     for task in state.tasks_by_timestamp():
#         print(task)
