from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserApp


# Create your forms here.

class NewUserAppForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserApp
        fields = (
        'code', 'name', 'surname', 'password', 'email', 'fiscalCode', 'birthDate', 'birthPlace', 'residence', 'smartContractList',
        'extensions')
        widgets = {
            'password': forms.PasswordInput()  # rendi il campo password un campo di input di tipo password
        }

    def save(self, commit=True):
        user = super(NewUserAppForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
