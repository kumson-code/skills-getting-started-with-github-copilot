from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "student@mergington.edu"

    signup_response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        f"/activities/Chess Club/participants/{email}"
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activities = activities_response.json()["Chess Club"]
    assert email not in activities["participants"]
