from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Заголовок')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=widgets.Textarea)
    author = forms.CharField(max_length=50, required=True, label='Автор')
