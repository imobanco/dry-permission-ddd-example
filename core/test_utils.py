import base64

from django.conf import settings
from django.test.runner import DiscoverRunner
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = None

    def get_path(self, id_detail=None, action=None, _filter=None):
        if not self.endpoint:
            raise AttributeError("Endpoint não definido")
        path = f"/{self.endpoint}/"
        if id_detail:
            path += f"{id_detail}/"
        if action:
            path += f"{action}/"
        if _filter:
            path += f"?{_filter}"
        return path


class BaseAPIAuthTestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.user = None
        self.password = None

    @property
    def auth(self):
        return {"HTTP_AUTHORIZATION": self.auth_header}

    @property
    def basic_auth_string(self):
        return f"{self.user.username}:{self.password}"

    @property
    def auth_token(self):
        return base64.b64encode(self.basic_auth_string.encode()).decode()

    @property
    def auth_header(self):
        return f"Basic {self.auth_token}"

    def set_user(self, user, password):
        self.user = user
        self.password = password


class MyTestSuiteRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        settings.TEST = True
        super(MyTestSuiteRunner, self).__init__(*args, **kwargs)
