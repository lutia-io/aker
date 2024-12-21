from drf_standardized_errors.handler import ExceptionHandler
from django.core.exceptions import ValidationError as DjValidationError
from core.errors import ValidationError


class ExceptionHandler(ExceptionHandler):
    def convert_known_exceptions(self, exc: Exception) -> Exception:
        if isinstance(exc, DjValidationError):
            return ValidationError(detail=exc.messages)
        else:
            return super().convert_known_exceptions(exc)
