from django import forms
from schema.models import Schema
from core.forms import PrettyJSONEncoder


class SchemaChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = Schema
        fields = "__all__"

    definition = forms.JSONField(encoder=PrettyJSONEncoder, required=True)
