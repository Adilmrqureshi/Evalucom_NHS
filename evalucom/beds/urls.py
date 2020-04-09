from django.urls import path

from . import views

app_name='beds'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('add_bed/<int:home_id>', views.add_bed, name="add_bed"),
    path('<int:offset>/', views.voyage, name='voyage')
]