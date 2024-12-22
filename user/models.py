from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.get_full_name()
