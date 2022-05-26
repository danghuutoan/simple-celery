## Broker settings.
broker_url = "amqp://guest@queue:5672//"

# List of modules to import when the Celery worker starts.
imports = ("task",)

## Using the database to store task state and results.
result_backend = "amqp://"

# task_annotations = {"task.add": {"rate_limit": "10/s"}}

