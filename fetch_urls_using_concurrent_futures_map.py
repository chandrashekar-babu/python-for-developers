#from concurrent.futures import ThreadPoolExecutor as Executor
from concurrent.futures import ProcessPoolExecutor as Executor

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
    work = []
    with Executor(max_workers=10) as pool:

        start = time.time()
        result = pool.map(fetch_url_status, urls)
    
    end = time.time()

    print(f"Total time taken: {end - start} seconds")