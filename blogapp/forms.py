from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "author", "placeholder": "Your Name"
    }))
    body = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        "class":"form-control", "id": "body", "placeholder": "Comment Here"
    }))
    class Meta:
        model = Comment
        fields = ['author', 'body',]
