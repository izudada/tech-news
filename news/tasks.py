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

