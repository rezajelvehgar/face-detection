from fastapi import FastAPI

app = FastAPI(
    title="Face Detection API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)