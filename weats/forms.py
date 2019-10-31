from django import forms
from .models import UserInfo


class PostForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('name', 'email', 'location')
