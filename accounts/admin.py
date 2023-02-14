from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
# UserAdmin.fieldsets[0][1]["fields"] = ("username", "username", "password")
# UserAdmin.fieldsets[2][1]["fields"] = (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "is_special",
#                     "special_user"
#                     "groups",
#                     "user_permissions",
#                 )

# UserAdmin.list_display = ("username", "username", "email", "first_name", "last_name", "is_active", "is_special")



class AccountUserAdmin(UserAdmin):

    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    'special_user',
                    # "is_special",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('username',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    # fieldsets = () # make password read-only

admin.site.register(User, AccountUserAdmin)

admin.site.unregister(Group)
