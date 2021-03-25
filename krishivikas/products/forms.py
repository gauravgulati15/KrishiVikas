from django import forms
from .models import ProductComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = (
            'author',
            'content',
        )
