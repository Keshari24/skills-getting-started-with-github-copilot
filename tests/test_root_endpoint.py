"""
Tests for the root endpoint and redirect behavior.
"""


def test_root_redirects_to_index(client):
    response = client.get("/", allow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_root_follow_redirect_returns_index(client):
    response = client.get("/", allow_redirects=True)

    assert response.status_code == 200
    assert "Mergington High School" in response.text
