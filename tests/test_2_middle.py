import pytest
import requests

URL = "https://petstore.swagger.io"
ENDPOINT = "/v2/pet/findByStatus"


@pytest.mark.parametrize("state", "expected", [
    ('avaliable', 690),
    ('pending', 10),
    ('sold', 10)
])
def test_2_middle(state, expected):
    # 1 Act
    """"curl -X 'GET' \
  'https://petstore.swagger.io/v2/pet/findByStatus?status=available' \
  -H 'accept: application/json'"""

    CONDITION = {"status": f'{state}'}
    HEADERS = {'accept': 'application/json'}
    swagger_url = f'{URL}{ENDPOINT}'

    # Arrange
    response = requests.get(url=swagger_url,
                            headers=HEADERS,
                            params=CONDITION)
    response.raise_for_status()
    pet_list = response.json()
    pet_count = len(pet_list)
