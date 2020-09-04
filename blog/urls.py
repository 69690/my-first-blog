from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('stories/story1', views.story1, name='story1'),
    # path('stories/story2', views.story2, name='story2'),
    # path('stories/story3', views.story3, name='story3'),

    path('story/<int:pk>/', views.post_detail, name='post_detail'),
    path('about', views.about, name='about'),
]