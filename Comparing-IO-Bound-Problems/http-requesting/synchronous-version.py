'''Average runtime 12.79 seconds on my computer'''

import requests
from timeit import default_timer as timer


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.python.org/",
        "https://www.google.com/",
    ] * 80
    start_time = timer()
    download_all_sites(sites)
    elapsed = timer() - start_time
    print(f"Downloaded {len(sites)} in {elapsed:.2f} seconds")
