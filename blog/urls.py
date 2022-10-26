from django.urls import path
from blog.views import show_post, post_detail, upload, show_json, addUpvote, add_post, addDownvote

app_name = 'blog'

urlpatterns = [
    path('', show_post, name='show_post'),
    path('details/<int:id>', post_detail, name='post_detail'),
    path('add-post/', upload, name='upload'),
    path('json/', show_json, name='show_json'),
    path('updateUpvote/<int:id>', addUpvote, name='addUpvote'),
    path('updateDownvote/<int:id>', addDownvote, name='addDownvote'),
]