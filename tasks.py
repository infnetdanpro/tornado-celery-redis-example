from celery import Celery
from time import sleep

app = Celery('tasks', broker='redis://localhost:6379//')

@app.task
def results(x, y):
    return 'Results'

@app.task
def prior(x, y):
    return 'Prior'

@app.task
def rating(x, y):
    return 'Rating'

@app.task
def main(x):
    results.delay(1, 1)
    sleep(1)
    prior.delay(2, 2)
    sleep(2)
    rating.delay(3, 3)
    return 'End'
