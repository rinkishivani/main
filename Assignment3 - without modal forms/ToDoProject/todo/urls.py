from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('home/<int:pk>/task', views.task, name="task"),
    path('home/<int:pk>/delete', views.delete, name="delete"),
    path('home/new-task', views.create, name="create-task"),
    path('home/<int:pk>/update-task', views.update, name="update-task"),
    path('home/<int:pk>/soft-delete', views.soft_delete, name="soft-delete"),
    path('home/trash', views.trash, name="trash"),
    path('home/<int:pk>/restore', views.restore, name="restore"),
    # path('home/<int:pk>', views.delete, name="delete"),
]
