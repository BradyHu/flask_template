from celery import task, shared_task


@task
def example(text):
    print(f'call celery :{text}')
    return f'call celery :{text}'
