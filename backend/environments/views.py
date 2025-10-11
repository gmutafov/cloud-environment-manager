from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from environments.forms import EnvironmentForm
from environments.models import Environment, ActivityLog


class EnvironmentListView(LoginRequiredMixin, ListView):
    model = Environment
    template_name = "environments/environment_list.html"
    context_object_name = "environments"

    def get_queryset(self):
        return Environment.objects.filter(owner=self.request.user)


class EnvironmentCreateView(LoginRequiredMixin, CreateView):
    model = Environment
    template_name = "environments/environment_form.html"
    form_class = EnvironmentForm
    success_url = reverse_lazy('environment_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        ActivityLog.objects.create(
            environment=self.object,
            user=self.request.user,
            action="created this environment"
        )
        return response


class EnvironmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Environment
    form_class = EnvironmentForm
    template_name = 'environments/environment_form.html'  # Reuse create form
    success_url = reverse_lazy('environment_list')

    def get_queryset(self):
        return Environment.objects.filter(owner=self.request.user)

    def test_func(self):
        environment = self.get_object()
        return environment.owner == self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        ActivityLog.objects.create(
            environment=self.object,
            user=self.request.user,
            action="updated this environment"
        )
        return response

class EnvironmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Environment
    template_name = 'environments/environment_confirm_delete.html'
    success_url = reverse_lazy('environment_list')

    def get_queryset(self):
        return Environment.objects.filter(owner=self.request.user)

    def test_func(self):
        environment = self.get_object()
        return environment.owner == self.request.user

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        ActivityLog.objects.create(
            environment=obj,
            user=request.user,
            action="deleted this environment"
        )
        return super().delete(request, *args, **kwargs)


class EnvironmentDetailView(LoginRequiredMixin, DetailView):
    model = Environment
    template_name = 'environments/environment_detail.html'
    context_object_name = 'environment'

    def get_queryset(self):
        return Environment.objects.filter(owner=self.request.user)

