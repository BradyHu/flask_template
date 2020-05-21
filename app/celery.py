from celery import Celery

from app.config import secure, settings

celery = Celery(
    settings.NAME,
    broker=secure.CELETY_BRPLER_URL,
    backend=secure.CELETY_RESULT_BACKEND
)
celery.autodiscover_tasks(['app.tasks'])

def make_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super(ContextTask, self).__call__(self, *args, **kwargs)

    celery.Task = ContextTask
