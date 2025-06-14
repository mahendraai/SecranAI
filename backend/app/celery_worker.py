from celery import Celery

celery_app = Celery(
    "scanner",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "tasks.scan_cloud_secrets": {"queue": "scans"}
}
