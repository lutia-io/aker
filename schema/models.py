from django.db import models
from core.models import BaseModel
from user.models import User
from organization.models import Organization


class Schema(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schemas")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="schemas"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["slug", "organization"],
                name="unique_schema_slug_per_organization",
            )
        ]

    def __str__(self):
        return self.name
