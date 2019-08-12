from app.oc import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    rv = client.get('/')
    assert '2019 - 1° cuatrimestre' in rv.data.decode('utf-8')
