from core.models import BaseModel
from django.db import models
from user.models import User
from organization.models import Organization


class Schema(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    definition = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schemas")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="schemas"
    )

    def __str__(self) -> str:
        return self.name
