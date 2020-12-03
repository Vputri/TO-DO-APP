from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from App import views
from register import views as v

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.listTask, name="task_list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
]