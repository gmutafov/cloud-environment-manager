from django.urls import path
from environments.views import EnvironmentListView, EnvironmentCreateView

urlpatterns = [
    path('', EnvironmentListView.as_view(), name='environment_list'),
    path('create/', EnvironmentCreateView.as_view(), name='environment_create'),
]
