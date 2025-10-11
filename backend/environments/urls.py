from django.urls import path, include
from environments.views import EnvironmentListView, EnvironmentCreateView, EnvironmentUpdateView, EnvironmentDeleteView

urlpatterns = [
    path('', EnvironmentListView.as_view(), name='environment_list'),
    path('create/', EnvironmentCreateView.as_view(), name='environment_create'),
    path('<int:pk>/', include([
        path('edit/', EnvironmentUpdateView.as_view(), name = 'environment_edit'),
        path('delete/', EnvironmentDeleteView.as_view(), name = 'environment_delete'),
    ])),
]