from random import choice

import pytest

from clients.api_client import ApiClient


@pytest.fixture
def id_for_available_with_photo():
    data = {
        "status": 'available'
    }
    pet_list = ApiClient.get_find_by_status(params=data).json()
    animal_with_info = id_for_available_with_photo(pet_list)
    return choice(list(animal_with_info.keys))
