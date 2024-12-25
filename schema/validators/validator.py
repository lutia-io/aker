from jsonschema import Draft202012Validator, validators
from schema.validators.formats.uuid import UUIDFormat
from schema.validators.types.number import PositiveNumberType
from jsonschema.exceptions import ValidationError


class Validator:
    def __init__(self):
        self.types = self._get_custom_types()
        self.formats = self._get_custom_formats()
        self.validator = self._create_validator()

    def _get_custom_types(self):
        return [
            PositiveNumberType(),
        ]

    def _get_custom_formats(self):
        return [
            UUIDFormat(),
        ]

    def _create_validator(self):
        type_checker = Draft202012Validator.TYPE_CHECKER
        format_checker = Draft202012Validator.FORMAT_CHECKER

        for custom_type in self.types:
            type_checker = type_checker.redefine(
                custom_type.name(), custom_type.validate
            )

        for custom_format in self.formats:
            format_checker.checkers[custom_format.name()] = (
                custom_format.validate,
                (str,),
            )

        def validate_additional_type(validator, additionalType, instance, schema):
            for custom_type in self.types:
                if custom_type.name() == additionalType:
                    try:
                        custom_type.validate(instance)
                    except ValidationError as e:
                        yield e

        return validators.extend(
            Draft202012Validator,
            type_checker=type_checker,
            format_checker=format_checker,
            validators={"additionalType": validate_additional_type},
        )

    def validate(self, schema, data):
        self.validator(schema).validate(data)

    def validate_schema(self, schema):
        try:
            self.validator.check_schema(schema)
        except Exception as e:
            raise ValueError(f"Invalid JSON Schema: {str(e)}")
