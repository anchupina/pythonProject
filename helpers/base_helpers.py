def get_filtered_animal_name(pet_list: list) -> list:
    # get all name for animal in category
    count = list()
    for pet in pet_list:
        category = pet.get('category', None)
        if category and 'string' not in category.get('name'):
            count.append(category.get('name'))
    print(count)
    return count
