from django import forms
from .models import IdeaPost, CrewPost, Tag


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

class CrewPostModelForm(forms.ModelForm):
    class Meta:
        model = CrewPost
        fields = ['title', 'content', 'tags']       

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
                    'placeholder' : '내용을 입력하세요.'
                }
            ),
        }