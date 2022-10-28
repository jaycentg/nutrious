from django.urls import path
from blog.views import show_post, post_detail, upload, show_json, addUpvote, addDownvote, show_json_by_tag, show_json_by_id

app_name = 'blog'

urlpatterns = [
    path('', show_post, name='show_post'),
    path('details/', post_detail, name='post_detail'),
    path('add-post/', upload, name='upload'),
    path('json/', show_json, name='show_json'),
    path('json/<str:tag>', show_json_by_tag, name='show_json_by_tag'),
    path('json/id/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('updateUpvote/<int:id>', addUpvote, name='addUpvote'),
    path('updateDownvote/<int:id>', addDownvote, name='addDownvote'),
]