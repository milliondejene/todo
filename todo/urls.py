from django.contrib import admin
from django.urls import path
from todoApp.views import home, task_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', task_list, name='task_list'),
    path('', home, name='home'),  # Define path for the root URL
]
