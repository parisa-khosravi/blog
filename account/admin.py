from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):


    models = User
    list_display = ('email','is_active','is_staff','is_superuser')
    list_filter = ('is_superuser',)
    search_fields = ('email',)
    ordering = ('-created_date',)
    fieldsets = (
        ('Authentication',{
            'fields':(
                'email','password'
            )
        }),
        ('Permissions',{
            'fields':(
                'is_active','is_staff','is_superuser',
            )
        }),
        ('Group Permissions',{
            'fields':(
                'groups','user_permissions'
            )
        }),
        ('Importants Dates',{
            'fields':(
                'last_login',
            )
        })
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_active','is_staff','is_superuser')
        }),
    )


admin.site.register(User,CustomUserAdmin)