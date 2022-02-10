from __future__ import absolute_import, unicode_literals
from argparse import Namespace
import os

from pytz import timezone

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
app.conf.enable_utc = False
app.conf.update(timezone='Africa/lagos')

app.config_from_object(settings, namespace="CELERY")

#   Celery Beat Setting
app.conf.beat_schedule = {

}

app.autodiscover_tasks()

app.task(bind=True)
def debug_task(self):
    print(f"Receiving work {self.request}")