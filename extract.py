from api_secrets import API_KEY
import grequests
import time
import json
from bs4 import BeautifulSoup

start_time = time.time()

def create_urls(start, end):
    urls = []
    for number in range(start, end):
        urls.append(f'https://www.imdb.com/list/ls098063263/?sort=list_order,asc&st_dt=&mode=detail&page={number}')
    return urls

def gather_imdb_ids(urls):
    imdb_ids = []
    responses = grequests.map((grequests.get(url) for url in urls))
    for index, response in enumerate(responses):
        soup = BeautifulSoup(response.content, "html.parser")
        list_of_movies = soup.find('div', {'class':'lister-list'})
        rows = list_of_movies.find_all("h3")
        for row in rows:
            a_tag = row.find('a')
            id = a_tag['href'].split('/')[2]
            imdb_ids.append(id)
        
        print(f'Page {index + 1} done')

    return imdb_ids

def create_API_requests(ids):
    urls = []
    for id in ids:
        urls.append(f'http://www.omdbapi.com/?i={id}&apikey={API_KEY}')
    return urls

def collect_movie_details(urls):
    movie_details = {}
    responses = grequests.map((grequests.get(url) for url in urls))
    for index, response in enumerate(responses):
        movie_details[index] = response.json()
    with open('extracted/movie_details.txt', 'w') as f:
        f.write(json.dumps(movie_details))


urls = create_urls(1, 11)
ids = gather_imdb_ids(urls)
API_urls = create_API_requests(ids)
collect_movie_details(API_urls)