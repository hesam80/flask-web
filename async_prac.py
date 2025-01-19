import asyncio
import time
from main import say_after
#!/usr/bin/env python3
# countasync.py

async def main_advanced():
    #start_exec= time.perf_counter()
    #from asyncio import TaskGroup
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            count())

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

        print(f"finished at {time.strftime('%X')}")
        

#with asyncio.Runner() as runner:
    #runner.run(main_advanced())

async def count():
    print("One")
    #await asyncio.sleep(1)
    await sleep(1)
    print("Two")

async def main():
    start_exec= time.perf_counter()
    await asyncio.gather(main_advanced(), count(),say_after(1,'home'))
    end_exec=time.perf_counter()
    elapsed = end_exec-start_exec
    print(f"{__file__} executed in {elapsed:.6f} seconds.")


    
asyncio.run(main())
    