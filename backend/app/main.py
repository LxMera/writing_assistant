from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import writing

app = FastAPI(
    title="AI Writing Assistant API",
    description="API for rephrasing text in different writing styles",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(writing.router)

@app.get("/")
async def root():
    return {"message": "AI Writing Assistant API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}