from fastapi import FastAPI
from .file_route import router as files


def init_routes(app: FastAPI):
    app.include_router(files)