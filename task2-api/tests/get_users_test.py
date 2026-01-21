from jsonschema import validate
from jsonschema.exceptions import ValidationError
from utils.client import ReqresClient
from schemas.get_users_json_schema import GET_USERS_JSON_SCHEMA

def test_get_list_users():
    client = ReqresClient()
    response = client.get_users(page=2)

    # Proper request code
    assert response.status_code == 200

    body = response.json()

    # Schema validation (types + structure)
    try:
        validate(instance=body, schema=GET_USERS_JSON_SCHEMA)
    except ValidationError as e:
        pytest.fail(
            f"Schema validation failed at {list(e.path)}: {e.message}"
        )

    # Explicit task requirements
    assert body["data"][0]["last_name"]
    assert body["data"][1]["last_name"]

    assert len(body["data"]) <= body["total"]