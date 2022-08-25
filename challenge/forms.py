
from django import forms
from .models import Comment, ReComment

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


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', )