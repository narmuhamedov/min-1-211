from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
GENDER_TYPE = (
    ('М', 'М'),
    ('Ж', "Ж"),
    ('Не определился', "Не определился")
)

class RegistrationCustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender'
        )

    def save(self, commit=True):
        user = super(RegistrationCustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user