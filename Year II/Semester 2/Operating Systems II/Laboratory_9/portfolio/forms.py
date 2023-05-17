from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class NameForm(forms.Form):
    username = forms.CharField(label='exampleInputEmail1', max_length=100)
    password1 = forms.CharField(label='exampleInputPassword1', max_length=100)
    password2 = forms.CharField(label='exampleInputPassword2', max_length=100)
