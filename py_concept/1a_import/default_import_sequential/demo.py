# build-in module => sys.path (current direcroty => third party)
import os
import sys
from redis import Redis

print(sys.modules['os'])
# if rename the redis.py in current directory, it will show third party path
print(sys.modules['redis'])

