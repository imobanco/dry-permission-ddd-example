from core.rest_framework.viewsets import ServiceGenericViewSet
from core.rest_framework.mixins import (
    CreateServiceMixin,
    ListServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
)
from .serializers import UserSerializer
from ..services import UserService


class UserViewSet(
    CreateServiceMixin,
    ListServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
    ServiceGenericViewSet,
):
    """
    API endpoint that allows users to be viewed or edited.
    """

    service_class = UserService
    serializer_class = UserSerializer
    filter_fields = []
