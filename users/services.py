from core.services import ModelService, PermissionService
from .models import User


class UserService(ModelService, PermissionService):
    model = User

    def create(self, password=None, **kwargs):
        user = User(**kwargs)
        user.set_password(password)
        user.save()
        return user
