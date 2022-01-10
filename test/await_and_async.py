import asyncio
from random import randint


async def do_stuff(ip, port):
    print(f'About to open a connection to {ip}'.format(ip=ip))
    reader, writer = await asyncio.open_connection(ip, port)

    print(f'Connection open to {ip}'.format(ip=ip))
    await asyncio.sleep(randint(0, 5))
    