from django.db import models
from core.models import BaseModel


class PolicyDefinition(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    definition = models.JSONField(blank=False, null=False)

    class Meta:
        verbose_name = "Policy Definition"
        verbose_name_plural = "Policy Definitions"

    def __str__(self) -> str:
        return self.name
