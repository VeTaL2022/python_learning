import asyncio


async def print_nums():
    num = 1
    while True:
        print('Number', num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    time = 1
    while True:
        print('Time', time)
        time += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)


asyncio.run(main())
