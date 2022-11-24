from clients.api_client import ApiClient


# import allure

# @allure.title('Test title')

def test_7_fixture(id_for_available_with_photo):
    data = {
        "petId": id_for_available_with_photo
    }
    animal_info = ApiClient.get_find_by_id(params=data).json()
    print(animal_info)
    return animal_info
