from django.urls import path

from webapp.views import ForumListView, CreateForumView

app_name = 'webapp'

#webapp:index
urlpatterns = [
    path('', ForumListView.as_view(), name='index'),
path('add-forum/', CreateForumView.as_view(), name='add-forum'),

]