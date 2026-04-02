import os

from fastapi import FastAPI


app = FastAPI(title="memory")
memory_store: dict[str, str] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"service": "memory", "status": "ok"}


@app.get("/memory/{key}")
def get_memory(key: str) -> dict[str, str | None]:
    return {"key": key, "value": memory_store.get(key)}


@app.put("/memory/{key}")
def put_memory(key: str, value: str) -> dict[str, str]:
    memory_store[key] = value
    return {"status": "saved", "key": key, "value": value}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8004")))
