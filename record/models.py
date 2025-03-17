from django.db import models
from core.models import BaseModel
from schema.models import Schema
from user.models import User
from organization.models import Organization


class Record(BaseModel):
    data = models.JSONField(blank=False, null=False)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="records")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="records")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="records"
    )

    def __str__(self):
        return str(self.uuid)
