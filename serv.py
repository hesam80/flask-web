import time , os
import asyncio
import time
def __init__():
    print("hello")
    path = os.path()





async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")
#asyncio.run(main())
async def main2():
    start_task=time.perf_counter()
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
    #print(f"{__file__}execute")
    task_done=time.perf_counter()
    elapsed=task_done-start_task
    elapsed_miliseconds=elapsed*1000
    print(f"this task executed in {elapsed:.6f} seconds.")
    print(f"this task executed in {elapsed_miliseconds:.1f} miliseconds.")
asyncio.run(main2())

async def main_advanced():
    #from asyncio import TaskGroup
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

        print(f"finished at {time.strftime('%X')}")
        print(f"{__file__}execute")

#with asyncio.Runner() as runner:
    #runner.run(main_advanced())