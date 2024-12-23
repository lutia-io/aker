from core.models import BaseModel
from django.db import models
from user.models import User
from organization.models import Organization
from django.core.exceptions import ValidationError
from schema.validators.validator import Validator


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
            validator = Validator()
            validator.validate_schema(self.definition)
        except ValueError as e:
            raise ValidationError(
                f"Your definition is an invalid JSON Schema: {str(e)}"
            )
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
