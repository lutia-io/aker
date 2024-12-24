from abc import ABC, abstractmethod


class ValidatorType(ABC):
    @abstractmethod
    def name(self):
        """Returns the name of the custom type."""
        pass

    @abstractmethod
    def validate(self, value):
        """Validates the value against the custom type."""
        pass
