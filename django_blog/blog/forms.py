from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms
# from taggit.forms import TagWidget


class CustomUserCreationForm( UserCreationForm ) :
    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# class CommentForm (forms.ModelForm) :
#     class Meta :
#         model = Comment
#         fields = ['content']
#         widgets = {
#              'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }

# class PostForm(forms.Model) :
#     class Meta :
#         model = Post
#         fields = ['title', 'content', 'tags']
#         widgets = {
#             'tags': TagWidget(),
#         }
