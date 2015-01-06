from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#get environmental variables from heroku
app.conf.update(BROKER_URL=os.environ['REDISGREEN_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDISGREEN_URL'])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

