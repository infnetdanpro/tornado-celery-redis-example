# tornado-celery-redis-example
Little prototype project for Seendex


pip install celery[redis]
pip install redis
pip install tornado

docker pull redis
docker run -d --name dev-redis -p 6379:6379 -t -v redis
