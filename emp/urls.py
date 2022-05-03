"""learn_models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from .views import (EmployeeCreateView, EmployeeListView, 
                        EmployeeDetailView, EmployeeUpdateView,
                        MembershipCreateView, EmployeeDeleteView,
                        MembershipDeleteView,GroupListView,
                        GroupCreateView,GroupUpdateView, GroupDeleteView,
                        upload_file, download_file, FileDeleteView, DeletedEmployeeListView,
                        RoleCreateView,RoleListView, RoleDeleteView, RoleUpdateView
                        )

urlpatterns = [
    path('add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('list/', EmployeeListView.as_view(), name='employee-list'),
    path('detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),

    path('add-group/', GroupCreateView.as_view(), name='add-group'),
    path('list-groups/', GroupListView.as_view(), name='list-groups'),
    path('update-group/<int:pk>/', GroupUpdateView.as_view(), name='update-group'),
    path('delete-group/<int:pk>/', GroupDeleteView.as_view(), name='delete-group'),

    path('add-membership/<int:pk>/', MembershipCreateView.as_view(), name='add-membership'),
    path('delete-membership/<int:pk>/', MembershipDeleteView.as_view(), name='delete-membership'),

    path('upload-file/<int:pk>/', upload_file, name='upload-file'),
    path('delete-file/<int:pk>/', FileDeleteView.as_view(), name='delete-file'),
    path('download-file/<int:pk>/', download_file, name='download-file'),

    path('add-role/', RoleCreateView.as_view(), name='add-role'),
    path('list-role/', RoleListView.as_view(), name='list-role'),
    path('delete-role/<int:pk>/', RoleDeleteView.as_view(), name='delete-role'),
    path('update-role/<int:pk>/', RoleUpdateView.as_view(), name='update-role'),

    path('deleted-employees', DeletedEmployeeListView.as_view(), name='deleted-employees'),

]
