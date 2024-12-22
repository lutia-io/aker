from rest_framework import serializers
from record.models import Record
from jsonschema import validate, ValidationError as JSONSchemaValidationError


class RecordSerializer(serializers.ModelSerializer):
    schema = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    organization = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Record
        fields = [
            "uuid",
            "data",
            "schema",
            "user",
            "organization",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "uuid",
            "schema",
            "user",
            "organization",
            "created_at",
            "updated_at",
        ]

    def validate_data(self, value):
        """Validate the JSON data against the schema definition."""
        schema = (
            self.instance.schema if self.instance else self.initial_data.get("schema")
        )
        if schema:
            try:
                validate(instance=value, schema=schema.definition)
            except JSONSchemaValidationError as e:
                raise serializers.ValidationError(
                    f"Invalid data for schema {schema.name}: {e.message}"
                )
        return value
