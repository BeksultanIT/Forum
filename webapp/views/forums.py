from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ForumForm
from webapp.forms.search import SearchForm

from webapp.models.forums import Forum


class ForumListView(ListView):
    template_name = 'forums/index.html'
    model = Forum
    context_object_name = 'forums'
    ordering = ['-created_at']
    paginate_by = 7


    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(title__icontains=self.search_value)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result["query"] = urlencode({"search": self.search_value})
            result['search'] = self.search_value
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


class CreateForumView(LoginRequiredMixin, CreateView):
    template_name = 'forums/create_forum.html'
    form_class = ForumForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateForumView(LoginRequiredMixin, UpdateView):
    template_name = "forums/update_forum.html"
    form_class = ForumForm
    model = Forum

class DeleteForumView(LoginRequiredMixin, DeleteView):
    model = Forum
    template_name = 'forums/delete_forum.html'
    success_url = reverse_lazy('webapp:index')

class DetailForumView(DetailView):
    template_name = 'forums/detail_forum.html'
    model = Forum