from django import forms
from .models import IdeaPost

class IdeaPostModelForm(forms.ModelForm):
    class Meta:
        model = IdeaPost
        fields = ['title', 'content']

        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'uploadTitle',
                    'placeholder' : '제목'
                }
            ),
            'content' : forms.Textarea(
                attrs = {
                    'class' : 'uploadTextarea',
                    'placeholder' : '아이디어를 입력해주세요'
                }
            )
        }
