from django.contrib import admin
from django.urls import path
import media_app.views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="media_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/home/',media_app.views.home,name="home"),
    path('media/form/',media_app.views.form,name="form"),
    path('',media_app.views.index,name="index"),
    path('media/mediaform/',media_app.views.mediaform,name='mediaform'),
    path('media/<int:pk>/edit/',media_app.views.edit,name='edit'),
    path('media/<int:pk>/remove/',media_app.views.remove,name='remove'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)