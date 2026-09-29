from django.urls import path




from . import views




urlpatterns = [
    path('', views.main, name='main'),
    path('projects', views.projects, name='projects'),
    path('my_able', views.my_able, name='my_able')
]