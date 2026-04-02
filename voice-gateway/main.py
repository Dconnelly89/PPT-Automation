import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app = FastAPI(title="voice-gateway")

automation_bridge_url = os.getenv("AUTOMATION_BRIDGE_URL", "http://automation-bridge:8003")


@app.get("/health")
def health():
    return {"service": "voice-gateway", "status": "ok"}


@app.post("/voice/ingest")
async def voice_ingest(payload: dict):
    text = payload.get("text", "")
    return {"received_text": text, "bridge_target": automation_bridge_url}


@app.get("/bridge/health")
async def bridge_health():
    url = f"{automation_bridge_url}/health"
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            resp = await client.get(url)
        return JSONResponse({"bridge_url": url, "status_code": resp.status_code})
    except Exception as exc:
        return JSONResponse({"bridge_url": url, "error": str(exc)}, status_code=503)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8005")))
