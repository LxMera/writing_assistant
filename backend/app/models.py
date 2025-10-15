from pydantic import BaseModel
from typing import Optional
from typing import Literal

class TextInput(BaseModel):
    text: str
    provider: Literal["openai", "azure", "claude"] = "azure"

class StyleResponse(BaseModel):
    professional: str
    casual: str
    polite: str
    social_media: str

class StreamResponse(BaseModel):
    style: str
    content: str
    is_complete: bool