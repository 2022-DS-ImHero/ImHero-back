from cProfile import label
import imp
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        
        widgets = {
            'content': forms.Textarea(attrs={
                'class': "commentform",
                'placeholder': '댓글을 작성하세요'
                }),
        }