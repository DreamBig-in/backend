from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from users import models


class UserAdmin(UserAdmin):
    fieldsets =  (
        (None, {"fields": ("username",)}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        
           (("User Course Details"), {
            "fields": (
                'tech_stack',
            ),
        }),
        (("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    # + (
    #     (("User Course Details"), {
    #         "fields": (
    #             'tech_stack',
    #         ),
    #     }),
    # )

    readonly_fields = ('date_joined', 'last_login'  , 'first_name', 'last_name', 'email' , 'username')
    


    # list_filter = ('is_staff', 'is_active', 'is_superuser')
    # search_fields = ('email', 'name')
    # ordering = ('email', 'name')
    # filter_horizontal = ()

admin.site.register(models.User , UserAdmin)