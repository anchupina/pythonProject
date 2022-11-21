from dataclasses import field, dataclass

from faker import Faker

fake = Faker()


@dataclass
class Pet(Place):
    id: int = None
    login: str = None
    first_name: str = field(default=None, compare=False)
    last_name: str = field(default=None, compare=False)


@classmethod
def random_init(cls, id=None, login):
    login = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    name = f"{last_name} {first_name}"

    return cls(first_name=first_name,
               login=f"{login}",
               last_name=last_name, name=name)
