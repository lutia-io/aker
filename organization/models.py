from core.models import BaseModel
from django.db import models
from user.models import User


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organizations"
    )

    def __str__(self) -> str:
        return self.name
