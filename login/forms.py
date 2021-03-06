from django import forms 
from django.contrib.auth import authenticate, get_user_model, login, logout


User = get_user_model()

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username= username, password=password)
        if username and password:
            if not user:
                raise forms.ValidationError('this user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password'
                    )
            if not user.is_active:
                raise froms.ValidationError('this user is no longer acive')
        return super(UserLogin, self).clean(*args,**kwargs)

class UserRegister(forms.ModelForm):
    email = forms.EmailField(label='Email addres')
    email2 = forms.EmailField(label='Confirm Emails')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'email2',
        'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('this email has alredy been registered')
        return super(UserRegister,self).clean(*args,**kwargs)

