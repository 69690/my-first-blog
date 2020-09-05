from django.urls import path
from . import views
from django.conf.urls import url 

urlpatterns = [
    path('', views.main, name="main"),
    path('home/', views.post_list, name='post_list'),
    # path('stories/story1', views.story1, name='story1'),
    # path('stories/story2', views.story2, name='story2'),
    # path('stories/story3', views.story3, name='story3'),

    path('story/<int:pk>/', views.post_detail, name='post_detail'),
    path('about', views.about, name='about'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    # url(r'^viewpost/$', views.viewpost, name='viewpost'),
    # url(r"viewpost/(?P<pk>\d+)/$", views.viewpost, name='viewpost'),
]