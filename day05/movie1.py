import requests
from fake_useragent import UserAgent
from lxml import etree
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
    e = etree.HTML(html)
    extra_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    return ['http://maoyan.com{}'.format(url) for url in extra_url]


def parse_info(html):
    e = etree.HTML(html)
    movie_name = e.xpath('//h3[@class="name"]/text()')[0]
    movie_types = e.xpath('//li[@class="ellipsis"][1]/text()')[0]
    movie_actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/a/text()')
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