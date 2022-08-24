from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm 

class UserCreationForm(forms.ModelForm):
    mentor_choice = (('Y', 'Mentor'), ('N', 'Mentee'))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
    is_mentor = forms.CharField(label='Mentor', widget=forms.RadioSelect(choices=mentor_choice))
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'name', 'is_mentor')
        widgets = {

            'email': forms.TextInput(attrs={
                'id':'email',                
                'placeholder': '이메일'
                }),
            'username': forms.TextInput(attrs={
                'id':'id',                
                'placeholder': '아이디'
                }),
            'password1': forms.PasswordInput(attrs={
                'id':'id_password1',  
                'placeholder': '영문, 숫자, 특수문자로 구성된 6~20자 비밀번호'
                }),
            'password2': forms.PasswordInput(attrs={
                'id':'id_password2', 
                'placeholder': '비밀번호 재입력'
                }),
            'name': forms.TextInput(attrs={
                'id':'name',  
                'placeholder': '이름'
                }),
                
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# 사용자의 자기 정보 변경 폼
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'name', 'is_mentor', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

# 로그인 폼
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password') # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
        widgets = {

            'username': forms.TextInput(attrs={
                'id':'id_username',                
                'placeholder': '아이디',
                }),
            'password': forms.PasswordInput(attrs={
                'id':'id_password',                
                'placeholder': '비밀번호'
                }),
            
                
        }