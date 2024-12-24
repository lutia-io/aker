from jsonschema.exceptions import ValidationError
from schema.validators.types.base import ValidatorType


class PositiveNumberType(ValidatorType):
    def name(self):
        return "positive-number"

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise ValidationError(
                f"Value '{value}' is not a number. Expected a positive number."
            )
        if value <= 0:
            raise ValidationError(
                f"Value '{value}' is not a positive number. Expected a value greater than 0."
            )
        return True
