from django.forms import forms

# Create forms here

class RegisterForm(forms.Form):
    class Meta:
        fields = '__all__'