from __future__ import absolute_import

import os

from celery import Celery
from mysite.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.development")

app = Celery("mysite")

app.config_from_object("mysite.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
