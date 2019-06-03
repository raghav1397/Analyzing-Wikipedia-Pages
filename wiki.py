import os

os.listdir("wiki")

print(len(os.listdir("wiki")))

with open("wiki/Furubira_District,_Hokkaido.html", 'r') as f:
    print(f.readlines())

import concurrent.futures
import time

pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

def read_data(filename):
    with open(filename) as f:
        data = f.read()
    return data

start = time.time()
filenames = ["wiki/{}".format(f) for f in os.listdir("wiki")]
content = pool.map(read_data, filenames)
content = list(content)
end = time.time()
print(end - start)
articles = [f.replace(".html", "").replace("wiki/", "") for f in filenames]

from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return str(soup.find_all("div", id="content")[0])

start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)
parsed = pool.map(parse_html, content)
parsed = list(parsed)
end = time.time()
print(end - start)

parsed[0]

def count_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = {}
    for tag in soup.find_all():
        if tag.name not in tags:
            tags[tag.name] = 0
        tags[tag.name] += 1
    return tags

start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)
tags = pool.map(count_tags, parsed)
tags = list(tags)

tag_counts = {}
for tag in tags:
    for k,v in tag.items():
        if k not in tag_counts:
            tag_counts[k] = 0
        tag_counts[k] += v
end = time.time()

print(end - start)
tag_counts

from bs4 import BeautifulSoup
from collections import Counter
import re

def count_words(html):
    soup = BeautifulSoup(html, 'html.parser')
    words = {}
    text = soup.get_text()
    text = re.sub("\W+", " ", text.lower())
    words = text.split(" ")
    words = [w for w in words if len(w) >= 5]
    return Counter(words).most_common(10)

start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)
words = pool.map(count_words, parsed)
words = list(words)

word_counts = {}
for wc in words:
    for word, count in wc:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
end = time.time()

print(end - start)
word_counts
