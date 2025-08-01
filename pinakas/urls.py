from django.contrib import admin
from django.urls import path
from pinakas import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   # urlpatterns = [
   # path('programme/', views.weekly_programme_view, name='weekly_programme'),
   # other paths...