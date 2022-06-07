import os
from celery import Celery
from celery.schedules import crontab
import celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yard.settings')
app = Celery('yard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Europe/Moscow'


app.conf.beat_schedule = {
    'start_bots': {
        'task': 'yandex.tasks.start',
        'schedule': crontab(hour=9, minute=30)
        # 'schedule': 30
    },
}

#celery -A yard worker -l info
#celery -A yard beat -l info