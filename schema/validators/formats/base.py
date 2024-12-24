from abc import ABC, abstractmethod


class ValidatorFormat(ABC):
    @abstractmethod
    def name(self):
        """Returns the name of the custom format."""
        pass

    @abstractmethod
    def validate(self, value):
        """Validates the value against the custom format."""
        pass
