from celery.schedules import crontab
import tasks 

beat_schedule = {
    'get_weather_every_minute': {
        'task': 'tasks.fetch_weather_of_cities',
        'schedule': 60,
        'args': ()
    }
}

timezone = 'UTC'
