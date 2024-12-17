from django.db import models
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-id",)
