from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models import TextInput, StyleResponse
from app.services.ai_service import AIService
import json
import asyncio

router = APIRouter(prefix="/api/writing", tags=["writing"])
ai_service = AIService()

@router.post("/rephrase", response_model=StyleResponse)
async def rephrase_text(input_data: TextInput):
    """Rephrase text in all styles at once"""
    try:
        result = await ai_service.rephrase_text(input_data.text, input_data.provider)
        return StyleResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rephrase-stream")
async def rephrase_text_stream(input_data: TextInput):
    """Stream rephrased text for each style"""
    async def generate():
        try:
            async for chunk in ai_service.rephrase_text_stream(input_data.text, input_data.provider):
                data = json.dumps(chunk)
                print(f"Sending chunk: {data}")  # ← AGREGAR DEBUG
                yield f"data: {data}\n\n"
                
        except Exception as e:
            print(f"Stream error: {str(e)}")  # ← AGREGAR DEBUG
            error_data = {
                "style": "error",
                "content": str(e),
                "is_complete": True
            }
            yield f"data: {json.dumps(error_data)}\n\n"
    
    return StreamingResponse(
        generate(), 
        media_type="text/event-stream",  # ← CAMBIAR DE "text/plain" A "text/event-stream"
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # ← AGREGAR ESTA LÍNEA
        }
    )

@router.get("/health")
async def health_check():
    return {"status": "healthy"}