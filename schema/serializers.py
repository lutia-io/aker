from rest_framework import serializers
from schema.models import Schema
from field.models import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ["id", "uuid", "name", "label", "type", "created_at", "updated_at"]


class SchemaSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Schema
        fields = [
            "id",
            "uuid",
            "name",
            "slug",
            "active",
            "fields",
            "created_at",
            "updated_at",
        ]
