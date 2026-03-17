import time
from api.utils.redis_client import redis_client

class RateLimiter:
    def __init__(self, limit=5, window=60):
        self.limit = limit
        self.window = window

    def is_allowed(self, user_id):
        key = f"rate_limit:{user_id}"
        current_time = int(time.time())

        # Increment request count
        count = redis_client.incr(key)

        # Set expiry for new key
        if count == 1:
            redis_client.expire(key, self.window)

        # Check limit
        if count > self.limit:
            return False
        
        return True
