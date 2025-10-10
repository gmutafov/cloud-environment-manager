from django.contrib import admin
from django.urls import path, include

import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.DashboardView.as_view(), name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('api/accounts/', include('accounts.api_urls')),
    path('environments/', include('environments.urls')),

]
