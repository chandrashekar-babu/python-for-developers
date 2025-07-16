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
    work = []
    with Executor(max_workers=10) as pool:

        start = time.time()
        for u in urls:
            result = pool.submit(fetch_url_status, u)
            work.append(result)

        while work:
            for w in work:
                if w.done():
                    stats.append(w.result())
                work.remove(w)

    end = time.time()

    print(f"Total time taken: {end - start} seconds")