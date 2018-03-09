from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=144, label='Nombre',)
    email = forms.CharField(max_length=144, label='Correo electronico',)
    subject = forms.CharField(max_length=144, label='Asunto',)
    message = forms.CharField(max_length=744, label='Mensaje',)