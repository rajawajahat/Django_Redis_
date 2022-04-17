from redis import Redis


class Cache:
    def __init__(self):
        self.time_to_expire_s = 300
        self.client = Redis(host="redis_server", port=6379)

    def set_key(self, key, value):
        self.client.set(key, value, ex=self.time_to_expire_s)

    def get_key(self, key):
        return self.client.get(key)
