from factory import Sequence, PostGenerationMethodCall
from factory.faker import Faker

from core.factories import BaseModelFactory
from users.models import User


class UserFactory(BaseModelFactory):
    class Meta:
        model = User

    is_staff = False
    is_superuser = False

    email = Sequence(lambda n: f"{Faker('user_name').generate()}{n}@example.net")
    username = Sequence(lambda n: f"{Faker('user_name').generate()}{n}")
    password = PostGenerationMethodCall("set_password", "password")
