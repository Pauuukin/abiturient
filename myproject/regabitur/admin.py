from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.utils.safestring import mark_safe


class UserInline(admin.TabularInline):
    model = CustomUser
    can_delete = False
   # list_display = ( 'phone_number','work_flag',' agreement_flag', 'complete_flag', 'sending_status', 'date_of_birth', 'patronymic')
    verbose_name_plural = 'Доп. информация'
    readonly_fields = ['date_of_birth', 'patronymic', 'phone_number']


class UserInlineDoc(admin.TabularInline):
    model = DocumentUser
    can_delete = False
    verbose_name_plural = 'Документы'
    readonly_fields = ['name_doc', 'doc','doc_url', ]

    def doc_url(self, obj):
        """для релизной версии путь"""
        str1 = 'https://abiturient.jurac.ru/static/media'
        sum = '{0}{1}'.format(str1, obj.doc.url)
        result = '<a href="{0}" target="_blank">открыть</a>'.format(sum)
        return mark_safe(result)


class UserAdmin(UserAdmin):
    model = User
    inlines = (UserInline, UserInlineDoc)
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined', 'email', 'status_doc')
    ordering = ('-date_joined',)
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

    def status_doc(self, obj):
        status = obj.custom.complete_flag
        work = obj.custom.work_flag
        success = obj.custom.success_flag
        result = None
        if obj.custom.sending_status == 'back':
            return ('Заявка отозвана')

        if status:
            result = "Документы поданы"
        elif status != 'True':
            result = " Не поданы "
        if success:
            return mark_safe(
                '<div style="width:100%%; height:100%%; background-color:green;">{0}</div>'.format(result))
        if work:
            return mark_safe('<div style="width:100%%; height:100%%; background-color:orange;">{0}</div>'.format(result))

        return mark_safe(result)
    # для сортировки:
    # status_doc.admin_order_field = 'custom__complete_flag'





# class DocUserInline(admin.StackedInline):
#     model = User
#     fk_name = 'id'
#     can_delete = False
#     verbose_name = 'Абитуриент'
#     fields = ['first_name', 'last_name', ]
#
#     #, 'patronymic', 'date_of_birth', 'sending_status', 'phone_number'


class DocUser(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'name_doc', 'doc_url', 'doc')
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
    def doc_url(self, obj):
        """для релизной версии путь"""
        str1 = 'https://abiturient.jurac.ru/static/media'
        sum = '{0}{1}'.format(str1, obj.doc.url)
        result = '<a href="{0}" target="_blank">открыть</a>'.format(sum)
        return mark_safe(result)


# Register your models here.
admin.site.register(DocumentUser, DocUser)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)