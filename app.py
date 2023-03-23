import redis


redis = redis.Redis(
    host='redis-16828.c246.us-east-1-4.ec2.cloud.redislabs.com',
    port=16828,
    password='fRl7GpEk8jLvlMqQUvTteOXfuEvV3xwF'
)
print(redis)