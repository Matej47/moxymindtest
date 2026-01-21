import pytest
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from utils.client import ReqresClient
from schemas.post_user_response_json_schema import POST_USER_RESPONSE_JSON_SCHEMA


# Load test data from JSON file
with open("task2-api/tests/testdata/create_user_data.json") as f:
    test_data = json.load(f)

# Iterate over test data
@pytest.mark.parametrize("payload", test_data)
def test_create_user(payload):
    client = ReqresClient()
    
    # Limit for response time in seconds
    RESPONSE_TIME_LIMIT = 0.1

    response = client.create_user(payload)

    # Proper request & HTTP code
    assert response.status_code == 201

    # Response time check
    assert response.elapsed.total_seconds() < RESPONSE_TIME_LIMIT

    body = response.json()

    # Assert returned fields
    assert "id" in body and body["id"]
    assert "createdAt" in body and body["createdAt"]

    # Optional bonus: schema validation
    try:
        validate(instance=body, schema=POST_USER_RESPONSE_JSON_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed at {list(e.path)}: {e.message}")

    #Extra check: Assert returned name/job matches input
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
