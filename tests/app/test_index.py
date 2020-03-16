from app.oc import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_index(client):
    rv = client.get("/")
    assert "2019 - 1° cuatrimestre" in rv.data.decode("utf-8")


def test_link(client):
    rv = client.get("/").data.decode("utf-8")
    assert 'a href="/periodo?a=2019' in rv
    assert "c=1" in rv
