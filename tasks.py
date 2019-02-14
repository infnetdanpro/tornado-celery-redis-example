from celery import Celery
from time import sleep

app = Celery('tasks', broker='redis://localhost:6379//')

@app.task
def results(x, y):
    print('results section')
    sleep(2)
    r = (x + y) * 102313
    sleep(2)
    return r

@app.task
def prior(x, y):
    print('prior section')
    sleep(3)
    rating.delay(100, 100)
    return x+y

@app.task
def rating(x, y):
    print('rating section')
    sleep(10)
    return x*y