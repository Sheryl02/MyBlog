from .views import home, post_detail, create_post, post_update, delete_post, categoryView, likePost, addComment
from django.urls import path
from . import views
# from blogApp import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', home.as_view(), name='home'),
    path('post_detail/<int:pk>', post_detail.as_view(), name='post_detail'),
    path('create_post/', create_post.as_view(), name='create_post'),
    path('post_update/<int:pk>', post_update.as_view(), name='post_update'),
    path('delete_post/<int:pk>', delete_post.as_view(), name='delete_post'),
    path('category/<str:category>', categoryView, name='category'),
    path('like/<int:pk>', likePost, name='like_post'),
    path('post_detail/<int:pk>/add_comment/', addComment.as_view(), name='add_comment'),
]
