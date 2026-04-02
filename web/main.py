import os

from fastapi import FastAPI

app = FastAPI(title="web")
api_base_url = os.getenv("API_BASE_URL", "http://api:8000")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "web"}


@app.get("/")
def index() -> dict[str, str]:
    return {
        "service": "web",
        "status": "ok",
        "api_base_url": api_base_url,
        "message": "web service ready",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "3000")))
