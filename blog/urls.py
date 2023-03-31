from django.contrib import admin
from django.urls import path

from article.views import index, new_detail

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('new/<int:id>/', new_detail, name='new'),
]

