import pytest


@pytest.fixture
def body(user_action, feedback):
    body = {}
    body["user_action"] = user_action
    body["feedback"] = feedback

    return body
