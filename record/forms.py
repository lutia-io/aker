from typing import Any
from django import forms
from record.models import Record
from core.forms import PrettyJSONEncoder


class RecordChangeForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = Record
        fields = "__all__"

    data = forms.JSONField(encoder=PrettyJSONEncoder, required=True)
