from django.urls import path

from webapp.views import ForumListView, CreateForumView, UpdateForumView, DeleteForumView, DetailForumView
from webapp.views.comments import CreateCommentView, UpdateCommentView, DeleteCommentView

app_name = 'webapp'

#webapp:index
urlpatterns = [
    path('', ForumListView.as_view(), name='index'),
    path('add-forum/', CreateForumView.as_view(), name='add-forum'),
    path('forum/<int:pk>/update/', UpdateForumView.as_view(), name='update-forum'),
    path('forum/<int:pk>/delete/', DeleteForumView.as_view(), name='delete-forum'),
    path('forum/<int:pk>/', DetailForumView.as_view(), name='detail-forum'),

    path('forum/<int:pk>/add-comment/', CreateCommentView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='comment-delete'),

]