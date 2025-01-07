import asyncio


async def say_hello():
    print("Hello...")


if __name__ == "__main__":
    el = asyncio.get_event_loop()
    el.run_until_complete(say_hello())
    el.close()
