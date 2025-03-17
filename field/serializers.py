from rest_framework import serializers
from field.models import Field, FieldOption


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ["id", "uuid", "name", "label", "type", "created_at", "updated_at"]


class FieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = ["id", "uuid", "name", "label", "sort"]
