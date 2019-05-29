'''Average runtime 1.14 seconds on my computer -> The fastest solution!'''

import asyncio
from timeit import default_timer as timer
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.python.org/",
        "https://www.google.com/",
    ] * 80
    start_time = timer()
    asyncio.run(download_all_sites(sites))
    elapsed = timer() - start_time
    print(f"Downloaded {len(sites)} sites in {elapsed:.2f} seconds")