import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, AsyncMock

client = TestClient(app)

@pytest.fixture
def mock_openai_service():
    with patch('app.routers.writing.openai_service') as mock:
        mock.rephrase_text = AsyncMock(return_value={
            'professional': 'Professional version',
            'casual': 'Casual version',
            'polite': 'Polite version',
            'social_media': 'Social media version'
        })
        yield mock

def test_health_endpoint():
    response = client.get("/api/writing/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_rephrase_endpoint(mock_openai_service):
    response = client.post(
        "/api/writing/rephrase",
        json={"text": "Hello world"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "professional" in data
    assert "casual" in data
    assert "polite" in data
    assert "social_media" in data

def test_rephrase_empty_text():
    response = client.post(
        "/api/writing/rephrase",
        json={"text": ""}
    )
    
    assert response.status_code == 422  # Validation error