from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.detail, name='detail'),
    path('add/', views.add_game, name='add_game'),
    path('update/<int:id>/', views.update_game, name='update_game'),
    path('delete/<int:id>/', views.delete_game, name='delete_game'),
]
