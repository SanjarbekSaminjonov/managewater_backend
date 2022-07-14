from django.contrib.auth.forms import (
    UserCreationForm as UserCreationFormBase,
    UserChangeForm as UserChangeFormBase
)

from .models import User


class UserCreationForm(UserCreationFormBase):
    class Meta(UserCreationFormBase):
        model = User
        fields = (
            'username',
        )


class UserChangeForm(UserChangeFormBase):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'region',
            'city',
            'org_name',
            'is_master'
        )
