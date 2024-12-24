from core.models import BaseModel
from django.db import models
from user.models import User
from organization.models import Organization
from schema.models import Schema
from django.core.exceptions import ValidationError
from schema.validators.validator import Validator


class Record(BaseModel):
    data = models.JSONField()
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="records")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="records")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="records"
    )

    def __str__(self) -> str:
        return str(self.uuid)

    def clean(self):
        try:
            validator = Validator()
            validator.validate(self.schema.definition, self.data)
        except Exception as e:
            raise ValidationError(
                f"Invalid data for schema {self.schema.name}: {str(e)}"
            )
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
