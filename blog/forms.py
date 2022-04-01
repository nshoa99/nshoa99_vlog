from django import forms
from django.db import models
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "user_email": "Your email",
            "text": "Your comment"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must be filled"}
        }
