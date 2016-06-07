from django import forms
from .models import Comment
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='Имя отправителя')
    email = forms.EmailField(label='E-Mail отправителя')
    to = forms.EmailField(label='E-Mail получателя')
    comments = forms.CharField(required=False,
                               label='Комментарий',
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class MyMarkdownForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())
    content2 = MarkdownFormField()
