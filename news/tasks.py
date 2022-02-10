from django.template import base
from celery import shared_task
import requests


base_url = 'https://hacker-news.firebaseio.com/v0/'
max_id_url = base_url + 'maxitem.json'

# @shared_task(bind=True)
# def test_func(self):
#     for i in range(10):
#         print(i)
#     return "Done"

@shared_task(bind=True)
def published_news(self):
    response = requests.get(max_id_url)
    lower_bound = 1
    max_id = int(response.text)
    
    if lower_bound < max_id:
        for i in range(lower_bound, lower_bound + 10):

            request_next_100_news = requests.get(base_url + f'item/{i}.json?print=pretty')
            print(request_next_100_news.text)
            lower_bound += 100

    return 'Done'