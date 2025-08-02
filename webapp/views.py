from django.views.generic import ListView

from webapp.models.forums import Forum


class ForumListView(ListView):
    template_name = 'forums/index.html'
    model = Forum
    context_object_name = 'form'
    ordering = ['-created_at']
    paginate_by = 7