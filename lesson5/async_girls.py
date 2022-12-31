import asyncio
import time
import requests
import httpx
import uuid


def time_decor(func):
    def inner(*args, **kwargs):
        starting = time.time()
        func(*args, **kwargs)
        print(time.time() - starting)

    return inner


# def get_response(url):
#     return requests.get(url, allow_redirects=True)
#
#
# def write_file(resp: requests.Response):
#     file_name = resp.url.split('/')[-1]
#     with open(file_name, 'wb') as file:
#         file.write(resp.content)
#
#
# @time_decor
# def main():
#     url = 'https://loremflickr.com/320/240/girls'
#     for _ in range(50):
#         write_file(get_response(url))
#
#
# main()

def write_file(data):
    file_name = f'file-{uuid.uuid1()}.jpg'
    with open(file_name, 'wb') as file:
        file.write(data)


async def get_response(url, client):
    result = await client.get(url, follow_redirects=True)
    write_file(result.read())


async def start():
    url = 'https://source.unsplash.com/1600x900/?girls'
    # https://loremflickr.com/320/240/girls

    tasks = []
    async with httpx.AsyncClient() as client:
        for _ in range(50):
            task = asyncio.create_task(get_response(url, client))
            tasks.append(task)
        await asyncio.gather(*tasks)


@time_decor
def main():
    asyncio.run(start())


main()
