from celery import Celery

app = Celery('red_neuronal', broker='redis://localhost:6379', backend='redis://localhost:6379', include=['red_neuronal', ])