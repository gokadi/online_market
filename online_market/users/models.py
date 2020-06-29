from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserAddress(models.Model):
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    building = models.CharField(max_length=10, verbose_name='Дом')
    flat = models.CharField(max_length=11, verbose_name='Квартира')

    objects = models.Manager()

    def __str__(self):
        return ' '.join((self.city, self.street, self.building, self.flat))


class CustomUserManager(UserManager):
    def _create_user(self, email: str, password: str, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    email = models.EmailField(unique=True, primary_key=True)
    address = models.OneToOneField(
        UserAddress, on_delete=models.SET_NULL, related_name='user', null=True
    )
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Отчество'
    )
    phone = PhoneNumberField(region='RU', verbose_name='Телефон')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: list = []

    def __str__(self):
        return self.email
