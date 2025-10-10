from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from environments.models import Environment


class EnvironmentListView(LoginRequiredMixin, ListView):
    model = Environment
    template_name = "environments/environment_list.html"
    context_object_name = "environments"

    def get_queryset(self):
        return Environment.objects.filter(owner=self.request.user)


class EnvironmentCreateView(LoginRequiredMixin, CreateView):
    model = Environment
    template_name = "environments/environment_form.html"
    fields = ['name', 'description', 'environment_type', 'status']
    success_url = reverse_lazy('environment_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
