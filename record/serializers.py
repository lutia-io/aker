from rest_framework import serializers
from record.models import Record
from schema.validators.validator import Validator


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
        schema = (
            self.instance.schema if self.instance else self.initial_data.get("schema")
        )
        if schema:
            try:
                validator = Validator()
                validator.validate(schema.definition, value)
            except Exception as e:
                raise serializers.ValidationError(
                    f"Invalid data for schema {schema.name}: {str(e)}"
                )
        return value
