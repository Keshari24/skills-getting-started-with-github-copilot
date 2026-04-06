"""
Tests for the POST /activities/{activity_name}/signup endpoint.
"""

from urllib.parse import quote

from src.app import activities


def test_signup_success_adds_participant(client):
    email = "newstudent@mergington.edu"
    activity_name = quote("Chess Club", safe="")

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"
    assert email in activities["Chess Club"]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    email = "test@mergington.edu"
    activity_name = quote("Unknown Activity", safe="")

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_registration(client):
    email = "michael@mergington.edu"
    activity_name = quote("Chess Club", safe="")

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
