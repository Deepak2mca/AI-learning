"""
the execution of the program as following: 
batch 1: 5 items
Processing batch: 0
Processing batch: 1
Processing batch: 2
Processing batch: 3
Processing batch: 4
Finished processing batch: 0
Finished processing batch: 1
Finished processing batch: 2
Finished processing batch: 3
Finished processing batch: 4
batch 2: 5 items
Processing batch: 5
Processing batch: 6
Processing batch: 7
Processing batch: 8
Processing batch: 9
Finished processing batch: 5
Finished processing batch: 6
Finished processing batch: 7
Finished processing batch: 8
Finished processing batch: 9
batch 3: 2 items
Processing batch: 10
Processing batch: 11
Finished processing batch: 10
Finished processing batch: 11
"""

import asyncio
import time

async def process_batch(batch):
    print(f"Processing batch: {batch}")
    await asyncio.sleep(1)  # Simulate some processing time
    print(f"Finished processing batch: {batch}")
    return f"Result of batch {batch}"

async def runner(items,batch_size):
    out = []
    for i in range(0, len(items), batch_size):
        chunk = items[i:i + batch_size]
        print(f"batch {i // batch_size + 1}: {len(chunk)} items")
        out.extend(await asyncio.gather(*(process_batch(x) for x in chunk)))
        await asyncio.sleep(0.1)  
        
    return out  # the polite pause between batches

start = time.time()
asyncio.run(runner(list(range(12)), batch_size=5))
print(f"done in {time.time() - start:.1f}s")
