from django.db import models
from core.models import BaseModel


class PolicyDefinition(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    definition = models.JSONField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name
