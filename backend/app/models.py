from pydantic import BaseModel
from typing import Optional

class TextInput(BaseModel):
    text: str

class StyleResponse(BaseModel):
    professional: str
    casual: str
    polite: str
    social_media: str

class StreamResponse(BaseModel):
    style: str
    content: str
    is_complete: bool