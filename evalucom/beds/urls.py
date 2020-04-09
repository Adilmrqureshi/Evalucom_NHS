from django.urls import path

from . import views

app_name='beds'
urlpatterns = [ 
    path('<int:offset>/', views.voyage, name='voyage'),
    path('', views.voyage, name='voyage'),
    path('add_bed/<int:home_id>', views.add_bed, name="add_bed"),
    path('index', views.index, name="index")
]