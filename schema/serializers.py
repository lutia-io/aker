from rest_framework import serializers
from schema.models import Schema


class SchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = [
            "uuid",
            "name",
            "slug",
            "definition",
            "user",
            "organization",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "uuid",
            "slug",
            "created_at",
            "updated_at",
            "user",
            "organization",
        ]
