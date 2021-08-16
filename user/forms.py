from django import forms
class loginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı adı")
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
    

class registerForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı adı")
    password = forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Şifreyi Onaylayın.",widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler uyuşmuyor")
        values = {
            "username" : username,
            "password" : password
        }
        return values
    
