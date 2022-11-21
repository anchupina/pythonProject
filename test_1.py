from faker import Faker

fake = Faker()


def test_pet(cls):
    # print('pet')
    # fake = Faker('it_IT')
    # for _ in range(10):
    #     print(fake.name())

    # fake = Faker()
    # fake.random
    # fake.random.getstate()

    login = fake.user_name()
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    name = f"{last_name} {first_name} {middle_name}"

    return cls(first_name=first_name, middle_name=middle_name,
               login=f"{login}",
               last_name=last_name, name=name
               )
