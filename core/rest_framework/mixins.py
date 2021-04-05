from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class CreateServiceMixin(CreateModelMixin):
    """
    Sobreescrevemos o create para chamar o método create do Service,
    e não do serializer.
    """

    def perform_create(self, serializer):
        service = self.get_service()
        instance = service.create(**serializer.validated_data)
        new_serializer = self.get_serializer(instance)
        serializer._data = new_serializer.data


class DestroyServiceMixin(DestroyModelMixin):
    """
    Sobreescrevemos o destroy para chamar o método delete do Service, e não do object.
    """

    def perform_destroy(self, instance):
        service = self.get_service()
        service.delete(instance)


class ListServiceMixin(ListModelMixin):
    """
    Não precisamos sobreescrever a ação list.
    É apenas de leitura.
    """


class RetrieveServiceMixin(RetrieveModelMixin):
    """
    Não precisamos sobreescrever a ação retrieve.
    É apenas de leitura.
    """


class UpdateServiceMixin(UpdateModelMixin):
    """
    Sobreescrevemos o update para chamar o método update do service,
    e não do serializer.
    Não precisamos sobreescrever o partial_update, ele chama o update.
    """

    def perform_update(self, serializer):
        service = self.get_service()
        instance = serializer.instance
        service.update(instance, **serializer.validated_data)
        new_serializer = self.get_serializer(instance)
        serializer._data = new_serializer.data
