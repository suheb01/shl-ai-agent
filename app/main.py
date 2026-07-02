from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router

app = FastAPI(
    title="SHL AI Assessment Recommender",
    description="Conversational SHL Assessment Recommendation API",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SHL AI Assessment Recommender"
    }