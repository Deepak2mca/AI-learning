"""
the outcome of this demo is:

A start
B start
C start
A done after 1s
C done after 1s
B done after 2s
results (in order): ['A', 'B', 'C']
total: 2.0s
"""
import asyncio
import time


async def nap(name, seconds):
    print(f"{name} start")
    await asyncio.sleep(seconds)
    print(f"{name} done after {seconds}s")
    return name


async def main():
    results = await asyncio.gather(nap("A", 1), nap("B", 2), nap("C", 1))
    print("results (in order):", results)


start = time.time()
asyncio.run(main())
print(f"total: {time.time() - start:.1f}s")     # ~3s (the max), not 6s (the sum)
