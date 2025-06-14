from fastapi import APIRouter, HTTPException, Request
from tasks import scan_cloud_secrets
from celery.result import AsyncResult

router = APIRouter()

@router.post("/scan")
def start_scan(request: Request):
    body = request.json()
    cloud_type = body.get("cloud")
    credentials = body.get("credentials")

    if cloud_type not in ["aws", "azure", "gcp"]:
        raise HTTPException(status_code=400, detail="Unsupported cloud type")

    task = scan_cloud_secrets.delay(cloud_type, credentials)
    return {"task_id": task.id, "status": "started"}

@router.post("/cloud-connect")
def cloud_connect(request: Request):
    body = await request.json()
    provider = body.get("provider")

    # Store encrypted creds or trigger OAuth redirect logic
    return {"message": f"{provider} connection simulated"}


@router.get("/scan-status/{task_id}")
def scan_status(task_id: str):
    result = AsyncResult(task_id)
    return {
        "status": result.status,
        "result": result.result if result.ready() else None
    }