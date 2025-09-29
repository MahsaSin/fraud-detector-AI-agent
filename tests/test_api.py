# tests/test_api.py
from fastapi.testclient import TestClient
from app import app
import app as app_module 

client = TestClient(app)

def test_analyze_success(monkeypatch):
    # Patch the symbol used by the route
    monkeypatch.setattr(
        app_module,
        "run_fraud_agent",
        lambda q: {
            "rating": "HIGH",
            "score": 99,
            "reasons": ["Suspicious promise of high returns"],
            "evidence": [{"title": "Some site", "url": "https://example.com"}],
            "disclaimer": "Test disclaimer",
        },
    )

    response = client.post("/FraudDetective", json={"query": "fake query"})
    assert response.status_code == 200
    data = response.json()
    assert data["rating"] == "HIGH"
    assert data["score"] == 99
    assert "reasons" in data
    assert "evidence" in data
    assert "disclaimer" in data
