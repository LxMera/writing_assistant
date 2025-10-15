from openai import AsyncAzureOpenAI
from openai import AsyncOpenAI
import os
from typing import AsyncGenerator, Dict
import asyncio
from dotenv import load_dotenv
from anthropic import AsyncAnthropic

load_dotenv()

class AIService:
    def __init__(self):
        self.client = None
        
    async def _call_azure(self, prompt: str) -> str:
        self.client = AsyncAzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )        

        response = await self.client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
                    
        content = response.choices[0].message.content
        return content
    
    async def _stream_azure(self, prompt: str, style: str) -> AsyncGenerator:
        try:
            self.client = AsyncAzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version="2024-12-01-preview",
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
            )
            
            stream = await self.client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7,
                stream=True
            )
            
            content = ""
            async for chunk in stream:
                # Validación robusta
                if hasattr(chunk, 'choices') and chunk.choices:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        content += delta.content
                        yield {
                            "style": style,
                            "content": content,
                            "is_complete": False
                        }
                        await asyncio.sleep(0.05)
            
            # Yield final solo si hay contenido
            if content:
                yield {
                    "style": style,
                    "content": content,
                    "is_complete": True
                }
            else:
                yield {
                    "style": style,
                    "content": "No content generated",
                    "is_complete": True
                }
                
        except Exception as e:
            print(f"Azure stream error for {style}: {str(e)}")
            import traceback
            traceback.print_exc()
            yield {
                "style": style,
                "content": f"Error: {str(e)}",
                "is_complete": True
            }
            
    async def _call_openai(self, prompt: str) -> str:
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        response = await self.client.chat.completions.create(
            model = os.getenv("OPENAI_MODEL"),
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        return content
    
    async def _stream_openai(self, prompt: str, style: str) -> AsyncGenerator:
        try:
            self.client = AsyncOpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )
            
            stream = await self.client.chat.completions.create(
                model = os.getenv("OPENAI_MODEL"),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7,
                stream=True
            )
            
            content = ""
            async for chunk in stream:
                # Validación robusta
                if hasattr(chunk, 'choices') and chunk.choices:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        content += delta.content
                        yield {
                            "style": style,
                            "content": content,
                            "is_complete": False
                        }
                        await asyncio.sleep(0.05)
            
            # Yield final solo si hay contenido
            if content:
                yield {
                    "style": style,
                    "content": content,
                    "is_complete": True
                }
            else:
                yield {
                    "style": style,
                    "content": "No content generated",
                    "is_complete": True
                }
                
        except Exception as e:
            print(f"Azure stream error for {style}: {str(e)}")
            import traceback
            traceback.print_exc()
            yield {
                "style": style,
                "content": f"Error: {str(e)}",
                "is_complete": True
            }
            
    async def _call_claude(self, prompt: str) -> str:
        self.client = AsyncAnthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        response = await self.client.messages.create(
            model = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514"), 
            max_tokens=500,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.content[0].text
        return content
    
    async def _stream_claude(self, prompt: str, style: str) -> AsyncGenerator:
        try:
            self.client = AsyncAnthropic(
                api_key=os.getenv("ANTHROPIC_API_KEY")
            )

            content = ""

            async with self.client.messages.stream(
                model=os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514"),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7,
            ) as stream:
                async for event in stream:
                    if event.type == "content_block_delta" and hasattr(event.delta, "text"):
                        chunk = event.delta.text
                        content += chunk

                        yield {
                            "style": style,
                            "content": content,
                            "is_complete": False
                        }
                        await asyncio.sleep(0.05)

            # Yield final solo si hay contenido
            if content:
                yield {
                    "style": style,
                    "content": content,
                    "is_complete": True
                }
            else:
                yield {
                    "style": style,
                    "content": "No content generated",
                    "is_complete": True
                }

        except Exception as e:
            print(f"Claude stream error for {style}: {str(e)}")
            import traceback
            traceback.print_exc()
            yield {
                "style": style,
                "content": f"Error: {str(e)}",
                "is_complete": True
            }
    
    async def rephrase_text(self, text: str, provider: str = "azure") -> Dict[str, str]:
        """Rephrase text in all styles at once"""
        prompt = f"""
        Please rephrase the following text in these 4 different writing styles, using the same language as the Original text.  
        Return only the rephrased versions, one per line, in this exact format:

        Professional: [rephrased text]
        Casual: [rephrased text]
        Polite: [rephrased text]
        Social-media: [rephrased text]

        Original text: "{text}"
        """
        
        try:
            if provider == "openai":
                content = await self._call_openai(prompt)
            elif provider == "azure":
                content = await self._call_azure(prompt)
            elif provider == "claude":
                content = await self._call_claude(prompt)
            else:
                raise ValueError(f"Unknown provider: {provider}")
            
            return self._parse_response(content)
            
        except Exception as e:
            raise Exception(f"{provider.upper()} API error: {str(e)}")
    
    async def rephrase_text_stream(self, text: str, provider: str = "azure") -> AsyncGenerator[Dict[str, str], None]:
        """Stream rephrased text for each style"""
        styles = ["professional", "casual", "polite", "social_media"]
        
        for style in styles:
            prompt = self._get_style_prompt(text, style)
            
            try:
                if provider == "openai":
                    async for chunk in self._stream_openai(prompt, style):
                        yield chunk
                elif provider == "azure":
                    async for chunk in self._stream_azure(prompt, style):
                        yield chunk
                elif provider == "claude":
                    async for chunk in self._stream_claude(prompt, style):
                        yield chunk
                else:
                    raise ValueError(f"Unknown provider: {provider}")
                
            except Exception as e:
                yield {
                    "style": style,
                    "content": f"Error: {str(e)}",
                    "is_complete": True
                }
    
    def _get_style_prompt(self, text: str, style: str) -> str:
        style_instructions = {
            "professional": "formal, business-like tone suitable for corporate communication",
            "casual": "relaxed, informal tone like talking to friends",
            "polite": "courteous, respectful tone with polite language",
            "social_media": "trendy, engaging tone with emojis and social media language"
        }
        
        return f"""
        Rephrase this text in a {style_instructions[style]}:
        
        "{text}"
        
        Return only the rephrased version, nothing else.
        """
    
    def _parse_response(self, content: str) -> Dict[str, str]:
        """Parse the OpenAI response into a dictionary"""
        lines = content.strip().split('\n')
        result = {}
        
        for line in lines:
            if ':' in line:
                parts = line.split(':', 1)
                if len(parts) == 2:
                    style = parts[0].strip().lower().replace('-', '_')
                    text = parts[1].strip()
                    result[style] = text
        
        # Ensure all styles are present
        default_styles = {
            'professional': '',
            'casual': '',
            'polite': '',
            'social_media': ''
        }
        
        return {**default_styles, **result}