'''Average runtime 2.77 seconds on my computer'''

import concurrent.futures
import requests
import threading
from timeit import default_timer as timer


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.python.org/",
        "https://www.google.com/",
    ] * 80
    start_time = timer()
    download_all_sites(sites)
    elapsed = timer() - start_time
    print(f"Downloaded {len(sites)} in {elapsed:.2f} seconds")