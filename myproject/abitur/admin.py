from django.contrib import admin
from .models import *

#регистрируем модели БД в админпанели
admin.site.register(News)
admin.site.register(NewsFile)
admin.site.register(Orders)
admin.site.register(RecommendedList)
admin.site.register(SubmitDoc)
admin.site.register(OrdersMag)
admin.site.register(RecommendedListMag)
admin.site.register(SubmitDocMag)
admin.site.register(OrdersAsp)
admin.site.register(RecommendedListAsp)
admin.site.register(SubmitDocAsp)