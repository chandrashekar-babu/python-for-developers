import asyncio

async def foo():
    for i in range(10):
        print("foo: counting", i)
        await asyncio.sleep(1)

async def bar():
    for i in range(10):
        print("bar: counting", i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(foo(), bar())

asyncio.run(main())
