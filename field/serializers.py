from rest_framework import serializers
from field.models import Field, FieldOption


class FieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = ["uuid", "name", "label", "sort"]


class FieldSerializer(serializers.ModelSerializer):
    options = FieldOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = [
            "uuid",
            "name",
            "label",
            "type",
            "created_at",
            "updated_at",
            "options",
        ]
