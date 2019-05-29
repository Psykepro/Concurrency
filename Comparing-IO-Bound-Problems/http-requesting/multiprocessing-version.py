'''Average runtime 3.64 seconds on my computer'''

import requests
import multiprocessing
from timeit import default_timer as timer


session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.python.org/",
        "https://www.google.com/",
    ] * 80
    start_time = timer()
    download_all_sites(sites)
    elapsed = timer() - start_time
    print(f"Downloaded {len(sites)} in {elapsed:.2f} seconds")