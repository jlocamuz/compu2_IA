from celery import group
from tasks import add

job = group([
             add.s(2, 2),
             add.s(4, 4),
             add.s(8, 8),
             add.s(16, 16),
             add.s(32, 32),
])

result = job.delay()
result.ready()  # have all subtasks completed?
result.successful() # were all subtasks successful?
print(result.get())
