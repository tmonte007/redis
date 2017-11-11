#!/usr/bin/env python

import redis
import os

mypass = os.environ.get('REDIS_PASS')

rdb = redis.Redis(
    				host='redis-17163.c16.us-east-1-3.ec2.cloud.redislabs.com',
    				port=17163, 
    				password=mypass)


# create a key value pair
rdb.set('name', 'Thomas')
print rdb.get('name')
rdb.exists('name')
rdb.delete('name')

# Increment numbers
rdb.set("indexer", 1)
rdb.incr("indexer")

# Make the data expire after 10 seconds
rdb.expire("indexer", 10)


# Redist lists
rdb.lpush("rlist", "Tom", "Bill", "Fred")

# print one item
rdb.lrange("rlist", 1, 1)

# get an entire list
rdb.lrange("rlist", 0, len("rlist"))


# Redis hash where order is not preserved
rdb.hmset("employee", {'name': 'Tom', 'job': 'programmer', 'employeeid': 7})
rdb.hgetall("employee")
rdb.hget("employee", 'name')

# Close the connection when you are done.
rdb.Close()