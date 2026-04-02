import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="automation-bridge")


class BridgeRequest(BaseModel):
    action: str
    payload: dict | None = None


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "automation-bridge"}


@app.post("/dispatch")
def dispatch(request: BridgeRequest) -> dict:
    # Placeholder for future orchestration logic.
    return {"accepted": True, "action": request.action, "payload": request.payload}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "8003")))
