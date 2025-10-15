from main import greet_api


def test_greet_api_plain_call():
    assert greet_api("Monorepo") == {"message": "Hello, Monorepo!"}
