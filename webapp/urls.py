from django.urls import path

from webapp.views import ForumListView

app_name = 'webapp'

#webapp:index
urlpatterns = [
    path('', ForumListView.as_view(), name='index'),

]