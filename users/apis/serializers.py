from core.rest_framework.serializers import ServiceSerializer
from users.models import User


class UserSerializer(ServiceSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "id",
            "created_at",
            "updated_at",
            "resource_type",
        ]
