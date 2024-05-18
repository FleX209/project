from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('materials', views.materials, name='materials'),
    path('materials/<int:task_id>/', views.material_detail, name='material_detail'),
    path('signup/', views.signup, name='signup'),
    path('authors/', views.authors, name='authors'),
]
