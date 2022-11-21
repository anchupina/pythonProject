import pytest

from clients.api_client import ApiClient
from helpers.base_helpers import get_filtered_animal_name


# import allure

# @allure.title('Test title')
@pytest.mark.parametrize("state", "expected", [
    pytest.param('sold', 10, id='sold test'),
    pytest.param('available', 690, id='available test'),
])
def test_5_helper(state, expected):
    """

    :param state:
    :param expected:
    :return:
    """
    data = {
        "status": state
    }
    pet_list = ApiClient.get_find_by_status(params=data).json()
    animal_with_filter = get_filtered_animal_name(pet_list=pet_list)

    print(animal_with_filter)
    return animal_with_filter
