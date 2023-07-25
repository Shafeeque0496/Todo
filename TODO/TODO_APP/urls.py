from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import Tasklist,TaskCreate,TaskUpdate,TaskDelete,TaskDetailView,CustomLoginView,RegisterView



urlpatterns = [

    path('',CustomLoginView.as_view(),name='user-login'),
    path('register/',RegisterView.as_view(),name='user-register'),
    path('list/',Tasklist.as_view(),name='task'),
    path('create/',TaskCreate.as_view(),name='task-create'),
    path('update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('delete/<int:pk>',TaskDelete.as_view(),name='task-delete'),
    path('details/<int:pk>',TaskDetailView.as_view(),name='task-details'),
    path('logout/',LogoutView.as_view(),name='logout')

]