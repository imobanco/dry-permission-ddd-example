import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True

    @classmethod
    def get_service_class(cls):
        raise NotImplementedError("Implemente get_class_service")

    @classmethod
    def get_service(cls, *args, **kwargs):
        return cls.get_service_class()(*args, **kwargs)

    @property
    def service(self):
        return self.get_service()

    @property
    def content_type(self):
        from .services import ModelService

        return ModelService().get_content_type(self)

    @property
    def resource_type(self):
        # noinspection PyUnresolvedReferences
        return self._meta.object_name
