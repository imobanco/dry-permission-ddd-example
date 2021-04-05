from rest_framework.viewsets import GenericViewSet

from .mixins import (
    CreateServiceMixin,
    DestroyServiceMixin,
    ListServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
)


class ServiceGenericViewSet(GenericViewSet):
    """
    GenericViewSet que utiliza a camada service e não o model diretamente.
    O :attr:`.service` substitui o :attr:`.queryset`.
    """

    service_class = None

    def get_queryset(self):
        """
        Sobreescrevemos esse método para utilizar o atributo :attr:`.service`
        ao invés do :attr:`.queryset`.

        Returns:
            :class:`.QuerySet`
        """
        service = self.get_service()

        return service.list()

    def get_service_class(self):
        return self.service_class

    def get_service(self, *args, **kwargs):
        """
        Método para instânciar o service.

        É aqui que é feito o 'acoplamento' da camada View Com a camada Service.
        """
        return self.get_service_class()(*args, **kwargs)


class ServiceViewSet(
    CreateServiceMixin,
    DestroyServiceMixin,
    ListServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
    ServiceGenericViewSet,
):
    pass
