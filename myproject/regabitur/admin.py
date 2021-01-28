from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UserInline(admin.TabularInline):
    """Доп. форма для пользователей с информацией из model.CustomUser"""
    model = CustomUser
    can_delete = False
   # list_display = ( 'phone_number','work_flag',' agreement_flag', 'complete_flag', 'sending_status', 'date_of_birth', 'patronymic')
    verbose_name_plural = 'Доп. информация'
    readonly_fields = ['date_of_birth', 'patronymic', 'phone_number']


class UserInlineDoc(admin.TabularInline):
    """Доп. форма для пользователей с информацией из model.DocumentUser"""
    model = DocumentUser
    can_delete = False
    verbose_name_plural = 'Документы'
    readonly_fields = ['name_doc', 'doc', 'date_pub', 'doc_url', ]
    ordering = ('-date_pub', )

    def doc_url(self, obj):
        """для релизной версии путь"""
        str1 = 'https://abiturient.jurac.ru/static/media'
        sum = '{0}{1}'.format(str1, obj.doc.url)
        result = '<a href="{0}" target="_blank">открыть</a>'.format(sum)
        return mark_safe(result)


class UserAdmin(UserAdmin):
    """Представление модели User"""
    model = User
    inlines = (UserInline, UserInlineDoc)
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined', 'email', 'status_doc')
    list_filter = ('date_joined',)
    ordering = ('-date_joined',)
    readonly_fields = [
        'user_permissions',
        'groups',
        'is_active',
        'password',
        'last_login',
        'is_superuser',
        'is_staff'
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


class DocUser(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'name_doc', 'doc_url', 'doc')
    list_filter = ('date_pub',)
    readonly_fields = ('user', )


    def doc_url(self, obj):
        """для релизной версии путь"""
        str1 = 'https://abiturient.jurac.ru/static/media'
        sum = '{0}{1}'.format(str1, obj.doc.url)
        result = '<a href="{0}" target="_blank">открыть</a>'.format(sum)
        return mark_safe(result)
    # fieldsets = (
    #     (None, {
    #         'fields': ('name_doc', 'doc')
    #     }),
    #     ('Availability', {
    #         'fields': ('username', 'first_name')
    #     }),
    # )

    # inlines = [DocUserInline, ]



class CustomUserResource(resources.ModelResource):
    """Класс, формирующий dateset из админ-панели"""
    class Meta:
        model = CustomUser


class CustomUserResource(ImportExportModelAdmin):
    """Класс, реализующий выгрузку из админ-панели"""
    resource_class = CustomUserResource


# Register your models here.
admin.site.register(DocumentUser, DocUser)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(CustomUser, CustomUserResource)



# class DocumentUserResource(resources.ModelResource):
#     """Класс, формирующий dateset из админ-панели"""
#     class Meta:
#         model = DocumentUser
#
#
# class DocumentUserResource(ImportExportModelAdmin):
#     """Класс, реализующий выгрузку из админ-панели"""
#     resource_class = DocumentUserResource



# class DocUserInline(admin.StackedInline):
#     model = User
#     fk_name = 'id'
#     can_delete = False
#     verbose_name = 'Абитуриент'
#     fields = ['first_name', 'last_name', ]
#
#     #, 'patronymic', 'date_of_birth', 'sending_status', 'phone_number'


