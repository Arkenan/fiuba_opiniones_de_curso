import pytest
from app.oc import app

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    rv = client.get('/')
    assert 'Bienvenido' in str(rv.data)
