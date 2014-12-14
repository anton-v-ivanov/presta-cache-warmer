from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import time


def main(url):
    soup = BeautifulSoup(urlopen(url))
    tags = soup.find("div", id="sitemap_content").findAll("a")
    links = []
    for tag in tags:
        links.append(tag["href"])
    tags = soup.find("div", id="listpage_content").findAll("a")
    for tag in tags:
        links.append(tag["href"])
    fetch(links)


def fetch(urls):
    for url in urls:
        nf = urlopen(url)
        start = time.time()
        nf.read()
        end = time.time()
        nf.close()
        print("Warm up: {0}\t\tTime taken: {1} ms".format(url, round((end - start) * 1000)))


def _usage():
    print("Usage: python warmer.py http://example.com/sitemap")


if __name__ == "__main__":
    urlArg = sys.argv[-1]
    if not urlArg.lower().startswith("http"):
        _usage()
        sys.exit(-1)
    main(urlArg)