from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models import TextInput, StyleResponse
from app.services.openai_service import OpenAIService
import json
import asyncio

router = APIRouter(prefix="/api/writing", tags=["writing"])
openai_service = OpenAIService()

@router.post("/rephrase", response_model=StyleResponse)
async def rephrase_text(input_data: TextInput):
    """Rephrase text in all styles at once"""
    try:
        result = await openai_service.rephrase_text(input_data.text)
        return StyleResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rephrase-stream")
async def rephrase_text_stream(input_data: TextInput):
    """Stream rephrased text for each style"""
    async def generate():
        try:
            async for chunk in openai_service.rephrase_text_stream(input_data.text):
                yield f"data: {json.dumps(chunk)}\n\n"
                
        except Exception as e:
            error_data = {
                "style": "error",
                "content": str(e),
                "is_complete": True
            }
            yield f"data: {json.dumps(error_data)}\n\n"
    
    return StreamingResponse(
        generate(), 
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

@router.get("/health")
async def health_check():
    return {"status": "healthy"}