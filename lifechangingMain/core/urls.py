<<<<<<< HEAD
from . import views
from django.urls import path


urlpatterns = [
  path('donor/', views.donor, name='donor'),
  ]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors/', views.contributors, name='contributors'),
    path('donor/', views.donor, name='donor'),
    path('about/', views.about, name='about'),
]
>>>>>>> front-end
