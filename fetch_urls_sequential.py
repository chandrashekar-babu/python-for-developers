from concurrent.futures import ThreadPoolExecutor as Executor

from threading import current_thread as current
import time


def fetch_url_status(url):
    from urllib.request import urlopen
    from urllib.error import HTTPError
    print(f"fetch_url_status(): fetching {url}")
    try: 
        res = urlopen(url)
    except HTTPError as e:
        status = str(e).split()[2]
    else:
        status = res.code

    print(f"fetch_url_status(): fetched {url}: status={status}")
    return res.code

urls = [
    "https://www.python.org/",
    "https://www.chandrashekar.info/",
    "https://www.slashprog.com/",
    "https://pypi.org/",
    "https://docs.python.org/",
    "https://gnu.org/"
]

if __name__ == '__main__':
    
    stats = []

    start = time.time()
    for u in urls:
        status = fetch_url_status(u)
        stats.append(status)
    end = time.time()

    print(f"Total time taken: {end - start} seconds")