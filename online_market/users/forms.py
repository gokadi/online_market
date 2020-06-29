from django.contrib.auth import get_user_model, forms
from django.forms import ModelForm

from online_market.users.models import UserAddress

UserModel = get_user_model()


class UserAddressForm(ModelForm):
    class Meta:
        model = UserAddress
        fields = '__all__'


class UserRegisterForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (
            'email', 'first_name', 'last_name',
            'phone', 'password1', 'password2',
        )


class UserProfileForm(forms.UserChangeForm):
    password = None

    class Meta:
        model = UserModel
        fields = (
            'email', 'first_name', 'last_name', 'middle_name', 'phone',
        )
        exclude = ('password', )
