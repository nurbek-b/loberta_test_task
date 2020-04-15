import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_status_checker.settings')


app = Celery('url_status_checker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'get_status_every_10_min': {
        'task': 'main_app.tasks.check_url_status',
        'schedule': crontab(minute='*/10')
    }
}