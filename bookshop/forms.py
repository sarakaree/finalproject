from django import forms
from bookshop.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image', 'pdf']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        description = cleaned_data.get('description')
        image = cleaned_data.get('image')
        pdf = cleaned_data.get('pdf')

        if not title or not author or not description or not image or not pdf:
            raise forms.ValidationError('All fields are required.')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = (
        ('author', 'Author'),
        ('publishing_house', 'Publishing House'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    author_id = forms.CharField(max_length=50, required=False)
    license = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'author_id', 'license']
