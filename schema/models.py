from core.models import BaseModel
from django.db import models
from user.models import User
from organization.models import Organization
from django.core.exceptions import ValidationError
from jsonschema import Draft7Validator, exceptions as jsonschema_exceptions


class Schema(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    definition = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schemas")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="schemas"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["slug", "organization"], name="unique_slug_per_organization"
            )
        ]

    def __str__(self) -> str:
        return self.name

    def clean(self):
        try:
            Draft7Validator.check_schema(self.definition)
        except jsonschema_exceptions.SchemaError as e:
            raise ValidationError(f"Your definition is an invalid JSON Schema: {e.message}")
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
