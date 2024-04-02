from django.contrib import admin
from django.urls import path, include
from courses import views
from rest_framework import routers

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='categories')
r.register('courses', views.CourseViewSet, basename='courses')
r.register('lessons', views.LessonViewSet, basename='lessons')
r.register('users', views.UserViewSet, basename='users')
r.register('comments', views.CommentviewSet, basename='comments')


urlpatterns = [
    path('', include(r.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
