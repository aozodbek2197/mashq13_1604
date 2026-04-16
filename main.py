# 1-mashq
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
# 2-mashq
from concurrent.futures import ThreadPoolExecutor

class Worker:
    def task(self, x):
        return x * x

w = Worker()
with ThreadPoolExecutor(max_workers=3) as ex:
    print(list(ex.map(w.task, [1,2,3])))
# 3-mashq
import asyncio

class AsyncService:
    async def run(self):
        await asyncio.sleep(1)
        print("Done")

async def main():
    s = AsyncService()
    await s.run()

asyncio.run(main())
# 4-mashq
import time

class RateLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.calls = []

    def allow(self):
        now = time.time()
        self.calls = [c for c in self.calls if now - c < 1]
        if len(self.calls) < self.limit:
            self.calls.append(now)
            return True
        return False
# 5-mashq
class Retry:
    def __init__(self, tries):
        self.tries = tries

    def run(self, func):
        for _ in range(self.tries):
            try:
                return func()
            except:
                continue
