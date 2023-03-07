from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ChatRoom, Message, UserProfile


class RoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'description']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'room']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
        

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ('bio',)
    
    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        profile = super(ProfileForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
