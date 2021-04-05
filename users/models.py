from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager
from core.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(
        "username",
        max_length=30,
        unique=True,
        help_text="Obrigatório. 150 caracteres ou menos. "
        "Letras, dígitos e @/./+/-/_ apenas.",
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": "Um usuário com esse nome já existe"},
    )

    email = models.EmailField("endereço de email", unique=True, help_text="email")

    password = models.CharField("senha", max_length=128, help_text="senha do usuário")

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="usuário tem acesso à interface admin?",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["email"]
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
