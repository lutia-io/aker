from typing import Any
from django import forms
from django.contrib.auth.forms import UserChangeForm
from user.models import User
from core.forms import PrettyJSONEncoder


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta(UserChangeForm.Meta):
        model = User

    profile = forms.JSONField(encoder=PrettyJSONEncoder, required=False)
