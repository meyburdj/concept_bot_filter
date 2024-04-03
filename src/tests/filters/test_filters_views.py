import pytest
import json

@pytest.fixture
def mock_orchestrate(mocker):
    """
    Fixture to mock the orchestrate_chatbot_pipeline function. This function
    does a pipeline of api calls and will be tested seperately
    """
    return mocker.patch('src.api.filters.views.orchestrate_chatbot_pipeline' , autospec=True)

def test_valid_post_request(test_client, mock_orchestrate):
    mock_orchestrate.return_value = "mocked result"

    response = test_client.post("/filter", json={
        "gradeLevel": "10",
        "academicTopic": "Math",
        "messages": [{"role": "user", "content": "Hello"}]
    })

    assert response.status_code == 200
    assert mock_orchestrate.called
    decoded_response = json.loads(response.data.decode())
    assert decoded_response == "mocked result"

@pytest.mark.parametrize("payload", [
    # Testing missing fields scenarios: 'messages', 'academicTopic', and 'gradeLevel'
    {"gradeLevel": "10", "academicTopic": "Math"},
    {"gradeLevel": "10", "messages": [{"role": "user", "content": "Hello"}]},
    {"academicTopic": "Math", "messages": [{"role": "user", "content": "Hello"}]}
])
def test_invalid_post_request_missing_fields(test_client, payload):
    response = test_client.post("/filter", json=payload)
    assert response.status_code == 400

def test_orchestrate_chatbot_pipeline_failure(test_client, mock_orchestrate):
    mock_orchestrate.side_effect = Exception("Mock exception")

    response = test_client.post("/filter", json={
        "gradeLevel": "10",
        "academicTopic": "Math",
        "messages": [{"role": "user", "content": "Hello"}]
    })

    assert response.status_code == 500
    assert "error" in response.json
    assert response.json["error"] == "Mock exception"
