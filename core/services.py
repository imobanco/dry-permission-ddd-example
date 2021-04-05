from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist, ProtectedError
from django.db import IntegrityError

from .exceptions import CustomException


class ModelService:
    """
    Classe controller Model da camada Service fazendo fronteira com a camada Model.

    Realiza a comunicação com o ORM do Django.
    """

    model = None

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def delete(self, instance):
        self.retrieve(instance.id)
        try:
            return instance.delete()
        except ProtectedError as e:
            raise CustomException("Não é possível deletar esse objeto!") from e

    def update(self, instance, **kwargs):
        """
        Esse update aciona os signals de save!
        """
        try:
            self.retrieve(instance.id)

            for key, value in kwargs.items():
                setattr(instance, key, value)

            instance.save()
            return instance
        except IntegrityError as e:
            raise CustomException("Não foi possível realizar essa alteração!") from e

    def retrieve(self, _id):
        return self.model.objects.get(id=_id)

    def list(self):
        return self.model.objects.all()

    def get(self, **kwargs):
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist as e:
            raise CustomException(
                f"Não existe um {self.model.__name__} com {kwargs}!"
            ) from e

    def filter(self, *args, **kwargs):
        return self.list().filter(*args, **kwargs)

    def first(self, *args, **kwargs):
        return self.filter(*args, **kwargs).first()

    def last(self, *args, **kwargs):
        return self.filter(*args, **kwargs).last()

    def count(self, *args, **kwargs):
        return self.filter(*args, **kwargs).count()

    def get_content_type(self, object_or_model=None):
        if object_or_model is None:
            object_or_model = self.model
        return ContentType.objects.get_for_model(object_or_model)


class PermissionService:
    def has_read_permission(self, **kwargs):
        return True

    def has_write_permission(self, **kwargs):
        return True

    def has_object_read_permission(self, obj, **kwargs):
        return True

    def has_object_write_permission(self, obj, **kwargs):
        return True
