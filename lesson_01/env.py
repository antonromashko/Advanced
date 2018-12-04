import os
from abc import ABCMeta
import fakeredis


class BaseBackend(metaclass=ABCMeta):
    def set(self):
        pass

    def get(self):
        pass


class FakeRedisBackend(BaseBackend):
    def __init__(self):
        self.redis = fakeredis.FakeStrictRedis()

    def set(self, key, value):
        return self.redis.set(key, value)


class OsEnvBackend(BaseBackend):
    def get(self, item):
        value = os.environ.get(item, '')
        return value


class MongoDBBackend(BaseBackend):
    pass


class Env:
    def __init__(self, backend='FakeRedis'):
        self.backend = backend

    def __getattr__(self, item):
        if self.backend == 'OS_ENV':
            return OsEnvBackend().get(item)


if __name__ == '__main__':
    obj = Env(backend='FakeRedis')
    obj.ALLUSERSPROFILE = 5
    print(obj.ALLUSERSPROFILE)
    o = FakeRedisBackend().get('adas', 5)
    print(o)

