"""A script that takes users' input and tranfer to database for Django app"""
from django import forms
from .models import UserInfo


class PostForm(forms.ModelForm):
    """A class that inherit from ModelForm"""
    class Meta:
        """A meta class that defines table to store database and the fields of the table"""
        model = UserInfo
        fields = ('name', 'email', 'location')
