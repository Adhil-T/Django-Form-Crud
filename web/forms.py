from django import forms
from .models import Book  # Assuming models.py is in the same app

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
