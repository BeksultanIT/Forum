from django.views.generic import ListView, CreateView

from webapp.forms import ForumForm
from webapp.models.forums import Forum


class ForumListView(ListView):
    template_name = 'forums/index.html'
    model = Forum
    context_object_name = 'forums'
    ordering = ['-created_at']
    paginate_by = 7


class CreateForumView(CreateView):
    template_name = 'forums/create_forum.html'
    form_class = ForumForm