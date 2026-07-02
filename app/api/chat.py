from fastapi import APIRouter

from app.models.schemas import ChatRequest, ChatResponse
from app.services.conversation_service import ConversationService

router = APIRouter()

conversation_service = ConversationService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    return conversation_service.chat(request)