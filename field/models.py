from django.db import models
from core.models import BaseModel
from user.models import User
from organization.models import Organization
from schema.models import Schema


FIELD_TYPES = (
    ("string", "String"),
    ("number", "Number"),
    ("datetime", "Date-time"),
    ("date", "Date"),
    ("time", "Time"),
    ("boolean", "Boolean"),
    ("email", "Email"),
)


class Field(BaseModel):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.CharField(choices=FIELD_TYPES, max_length=255)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="fields")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="fields_created_by"
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="fields"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "organization"],
                name="unique_field_name_per_organization",
            )
        ]

    def __str__(self):
        return self.name


class FieldOption(BaseModel):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    sort = models.PositiveIntegerField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="options")

    class Meta:
        ordering = ("sort",)
        constraints = [
            models.UniqueConstraint(
                fields=["name", "field"],
                name="unique_field_option_name_per_field",
            )
        ]

    def __str__(self):
        return self.name
