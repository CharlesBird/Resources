import asyncio
from asyncio import Lock, Queue
lock = Lock()
# with await lock
# asyncio with lock
# lock.release

total = 0

async def add():
    global total
    for i in range(1000000):
        total += i


async def desc():
    global total
    for i in range(1000000):
        total -= i


if __name__ == '__main__':
    loop  = asyncio.get_event_loop()
    tasks = [add(), desc()]
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)

