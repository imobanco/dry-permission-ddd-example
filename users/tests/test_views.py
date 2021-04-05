from rest_framework import status

from core.test_utils import BaseAPIAuthTestCase
from users.factories import UserFactory, User


class UsersAPITestCase(BaseAPIAuthTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = "users"

    # PATCH
    def test_patch(self):
        """
        Dado:
            - um usuário u1
        Quando:
            - u1 estiver autenticado
            - for atualizado u1
        Então:
            - a resposta deve ter sido 200
            - o u1 deve ter sido alterado
        """
        u1 = UserFactory(email="foo@bar.com")

        self.set_user(u1, "password")

        self.assertEqual(u1.email, "foo@bar.com")

        data = {"email": "bar@foo.com"}

        path = self.get_path(id_detail=u1.id)

        response = self.client.patch(path, data, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)

        u1.refresh_from_db()
        self.assertEqual(u1.email, "bar@foo.com")

    # LIST
    def test_list(self):
        """
        Dado:
            - três usuários quaisquer
        Quando:
            - o primeiro dos usuários está autenticado
            - for solicitado GET /users/
        Então:
            - a resposta deve ter sido 200
        """
        users = UserFactory.create_batch(3)
        self.assertEqual(User.objects.count(), 3)

        self.set_user(users[0], "password")

        path = self.get_path()

        response = self.client.get(path, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get("results")), 3, msg=response.data)

    # RETRIEVE
    def test_get(self):
        """
        Dado:
            - um usuário u1
            - uma pessoa p1 para u1
            - p1 está com vínculo
        Quando:
            - solicitado GET /users/u1.id/
        Então:
            - a resposta deve ter sido 200
            - o u1 deve ser retornado
        """
        u1 = UserFactory(email="foo@bar.com")
        self.assertEqual(User.objects.count(), 1)
        self.set_user(u1, "password")

        path = self.get_path(id_detail=u1.id)

        response = self.client.get(path, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

        self.assertEqual(response.data["id"], str(u1.id))
