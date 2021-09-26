import redis

conn = redis.Redis('redis-10000.re-cluster1.ps-redislabs.org','10000')
print(conn.ping())