"""
Tests for the DELETE /activities/{activity_name}/signup endpoint.
"""

from urllib.parse import quote

from src.app import activities


def test_unregister_success_removes_participant(client):
    email = "michael@mergington.edu"
    activity_name = quote("Chess Club", safe="")

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    email = "test@mergington.edu"
    activity_name = quote("Unknown Activity", safe="")

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_400_when_student_not_signed_up(client):
    email = "notregistered@mergington.edu"
    activity_name = quote("Chess Club", safe="")

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student not signed up for this activity"
