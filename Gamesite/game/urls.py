from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add/', views.add_game, name='add_game'),
    path('update/<int:id>/', views.update_game, name='update_game'),
    path('delete/<int:id>/', views.delete_game, name='delete_game'),
]
