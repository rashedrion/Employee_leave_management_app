from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('leave/', views.fetch_all_leaves, name="leaves"),
    path('leave/<int:id>/', views.fetch_leave_details, name="leave-details"),
    path('leave/add/', views.requet_new_leave, name="request-leave"),
    path('leave/<int:id>/edit/', views.edit_leave_request, name="edit-leave"),
    path('leave/<int:id>/delete/', views.delete_leave_request, name="delete-leave"),
]