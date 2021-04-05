from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = None

    def create(self, validated_data):
        raise NotImplementedError("Não use os métodos de criação do serializer!")

    def update(self, instance, validated_data):
        raise NotImplementedError("Não use os métodos de criação do serializer!")

    def save(self, **kwargs):
        raise NotImplementedError("Não use os métodos de criação do serializer!")

    @property
    def service(self):
        return self.Meta.model.get_service()
