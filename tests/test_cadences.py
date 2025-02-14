import pytest
from fastapi.testclient import TestClient
from main import app
from config.database import SessionLocal, Base, engine

client = TestClient(app)

# Setup and teardown for the database
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_add_email_cadence(setup_database):
    response = client.post(
        "/add_email_cadence/",
        json={"cadence_name": "Weekly Outreach", "timing": "Every Monday", "template": "Hello, this is a weekly update..."}
    )
    assert response.status_code == 200
    assert response.json()["cadence_name"] == "Weekly Outreach"

def test_modify_email_cadence(setup_database):
    response = client.put(
        "/modify_email_cadence/1",
        json={"timing": "Every Tuesday", "template": "Hello, this is an updated weekly email..."}
    )
    assert response.status_code == 200
    assert response.json()["timing"] == "Every Tuesday"
    assert response.json()["template"] == "Hello, this is an updated weekly email..."
