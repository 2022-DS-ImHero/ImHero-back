
from django import forms
from .models import Comment, ReComment, ComComment, SeComment

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

class ComCommentForm(forms.ModelForm):
    class Meta:
        model = ComComment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': "commentform",
                'placeholder': '댓글을 작성하세요'
                }),
        }
        

class SeCommentForm(forms.ModelForm):
    class Meta:
        model = SeComment
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