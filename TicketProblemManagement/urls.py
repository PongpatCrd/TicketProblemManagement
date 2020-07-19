"""TicketProblemManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import ticket_problem_management.views as tpm

import api.views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tpm.index),
    path('search/', tpm.problem_search, name="search"),
    path('login/', tpm._login, name="login"),
    path('logout/', tpm._logout, name="logout"),
    path('resolve/', tpm.resolve_problem_save, name="resolve_problem_save"),
    path('history/', tpm.history_search, name="history"),
    path('personal_member_detail/', tpm.personal_member_detail, name="personal_member_detail"),
    path('api/get_booking_detail', api.get_booking_detail),
]
