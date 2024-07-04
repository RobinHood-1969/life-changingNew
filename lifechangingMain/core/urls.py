from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
  path('', views.index, name='index'),
  path('donor/', views.donor, name='donor'),
  path('contributors/', views.contrib, name='contrib'),
  path('group_contributor/', views.groupcontrib, name='groupcontrib'),
  ]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)