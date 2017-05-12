from django import forms
from draceditor.fields import DraceditorFormField

class PostForm(forms.Form):
    description = DraceditorFormField()