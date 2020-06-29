from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from online_market.users.models import UserAddress, User

UserModel = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'is_active', )

    fieldsets = (
        ('Name', {'fields': ('first_name', 'last_name', 'middle_name')}),
        ('Contacts', {'fields': ('email', 'phone', 'address')}),
        ('Settings', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'first_name', 'last_name', 'email',
                'phone', 'password1', 'password2',
            ),
        }),
    )
    ordering = ('email', )

    def full_name(self, obj: User) -> str:
        return str(obj)

    full_name.short_description = 'Full name'  # type: ignore


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('full_address', )

    def full_address(self, obj: UserAddress) -> str:
        return str(obj)

    full_address.short_description = 'Address'  # type: ignore


admin.site.unregister(Group)

admin.site.register(UserModel, UserAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
