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

def test_add_custom_field(setup_database):
    response = client.post(
        "/add_custom_field/",
        json={"field_name": "key_contact", "field_type": "text", "field_value": "John Doe"}
    )
    assert response.status_code == 200
    assert response.json()["field_name"] == "key_contact"

def test_modify_custom_field(setup_database):
    response = client.put(
        "/modify_custom_field/1",
        json={"field_name": "primary_contact"}
    )
    assert response.status_code == 200
    assert response.json()["field_name"] == "primary_contact"
