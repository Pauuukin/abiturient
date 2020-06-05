from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *


class UserInline(admin.TabularInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'Доп. информация'
    readonly_fields = ['date_of_birth', 'patronymic', 'phone_number']


class UserInlineDoc(admin.TabularInline):
    model = DocumentUser
    can_delete = False
    verbose_name_plural = 'Документы'
    readonly_fields = ['name_doc', 'doc', ]


class UserAdmin(UserAdmin):
    inlines = (UserInline, UserInlineDoc)
    list_display = ('username', 'first_name', 'last_name', 'date_joined', 'email')
    readonly_fields = [
        'date_joined',
        'user_permissions',
        'groups',
        'date_joined',
        'is_active',
        'password',
        'last_login',
        'is_superuser',
        'is_staff',
        'username',
    ]


# class DocUserInline(admin.StackedInline):
#     model = User
#     fk_name = 'id'
#     can_delete = False
#     verbose_name = 'Абитуриент'
#     fields = ['first_name', 'last_name', ]
#
#     #, 'patronymic', 'date_of_birth', 'sending_status', 'phone_number'


class DocUser(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'name_doc', 'doc')
    list_filter = ('user_id',)
    readonly_fields = ('user', )
    # fieldsets = (
    #     (None, {
    #         'fields': ('name_doc', 'doc')
    #     }),
    #     ('Availability', {
    #         'fields': ('username', 'first_name')
    #     }),
    # )

    # inlines = [DocUserInline, ]


# Register your models here.
admin.site.register(DocumentUser, DocUser)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)