from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from accounts.forms import MyUserCreationForm
from accounts.models import Profile

# Create your views here.
User = get_user_model()

class RegisterView(CreateView):
    template_name = "user_create.html"
    model = User
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get('next')
        if not next:
            next = self.request.POST.get('next')
        if not next:
            next = reverse("webapp:index")
        return next

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user_obj'
    paginate_related_by = 12