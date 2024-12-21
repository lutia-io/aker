from typing import Any
from django import forms
from policy.models import PolicyDefinition
from core.forms import PrettyJSONEncoder


class PolicyDefinitionChangeForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = PolicyDefinition
        fields = "__all__"

    definition = forms.JSONField(encoder=PrettyJSONEncoder, required=True)
