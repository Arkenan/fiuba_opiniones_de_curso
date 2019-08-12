from app.oc import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    rv = client.get('/periodo?a=2019&c=1')
    assert 'Schwarz' in rv.data.decode('utf-8')
