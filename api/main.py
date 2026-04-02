from fastapi import FastAPI

app = FastAPI(title="API Service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "api"}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "api service ready"}
