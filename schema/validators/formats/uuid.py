from jsonschema.exceptions import ValidationError
from schema.validators.formats.base import ValidatorFormat
import uuid


class UUIDFormat(ValidatorFormat):
    def name(self):
        return "uuid"

    def validate(self, value):
        if not isinstance(value, str):
            raise ValidationError(
                f"Value '{value}' is not a valid UUID. Expected a string."
            )
        try:
            uuid.UUID(value)
        except ValueError:
            raise ValidationError(f"Value '{value}' is not a valid UUID.")
        return True
