from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('articles/add/', views.add, name='add'),
    path('articles/view/<int:id>', views.articleView, name='view'),
    path('articles/delete/<int:id>', views.articleDelete, name='delete'),
    path('articles/update/<int:id>', views.articleUpdate, name='update'),
]
