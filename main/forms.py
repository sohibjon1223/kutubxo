from django import forms
from .models import Book, News

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image']  # ✅ TO‘G‘RI
