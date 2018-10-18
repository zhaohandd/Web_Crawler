import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-agent': UserAgent().random
    }
    #sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.select('.channel-detail.movie-item-title > a')
    extra_url = []
    for a in all_a:
        extra_url.append(a['href'])
    # e = etree.HTML(html)
    # extra_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    return ['http://maoyan.com{}'.format(url) for url in extra_url]
    #return extra_url



def parse_info(html):
    soup = BeautifulSoup(html, 'lxml')
    movie_name = soup.select('h3.name')[0].text
    movie_types = soup.select('li.ellipsis')[0].text
    movie_actors = soup.select('li.celebrity.actor > div.info > a')
    # e = etree.HTML(html)
    # movie_name = e.xpath('//h3[@class="name"]/text()')[0]
    # movie_types = e.xpath('//li[@class="ellipsis"][1]/text()')[0]
    # movie_actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/a/text()')
    movie_actors = format_actors(movie_actors)
    return {
        'movie_name': movie_name,
        'movie_types': movie_types,
        'movie_actors': movie_actors
    }


def format_actors(movie_actors_a):
    actor_set = set()
    for movie_actor in movie_actors_a:
        actor_set.add(movie_actor.text.strip())
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