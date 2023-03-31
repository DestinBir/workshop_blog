from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from article.views import index
from . import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

