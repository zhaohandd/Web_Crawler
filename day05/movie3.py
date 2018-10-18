import requests
from fake_useragent import UserAgent
import re
from random import randint
from time import sleep


def get_html(url):
    headers = {
        'User-agent': UserAgent().random
    }
    sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    extra_url = re.findall(r'<a href="(/films/\d+)" target="_blank" data-act="movies-click" data-val="{movieId:\d+}">.*</a>', html)
    return ['http://maoyan.com{}'.format(url) for url in extra_url]


def parse_info(html):
    movie_name = re.findall(r'<h3 class="name">(.+)</h3>', html)[0]
    movie_types = re.findall(r'<li class="ellipsis">(.+)</li>', html)[0]
    movie_actors = re.findall(r'<li class="celebrity actor".+>\s+<a href="/films/cel.+>\s+<img.+>\s+</a>\s+<div.+>\s+<a.+>\s+(.+)\s+</a>', html)
    movie_actors = format_actors(movie_actors)
    return {
        'movie_name': movie_name,
        'movie_types': movie_types,
        'movie_actors': movie_actors
    }


def format_actors(movie_actors):
    actor_set = set()
    for movie_actor in movie_actors:
        actor_set.add(movie_actor.strip())
    return actor_set


def main():
    index_url = 'http://maoyan.com/films'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    print(movie_urls)
    for movie_url in movie_urls:
        movie_html = get_html(movie_url)
        movie = parse_info(movie_html)
        print(movie)


if __name__ == '__main__':
    main()