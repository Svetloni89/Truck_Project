from django.urls import path

from .views import *

urlpatterns = [
    path('', TrucksListView.as_view(), name='home page'),
    path('create/', TruckCreateView.as_view(), name='create page'),
    path('details/edit/<int:pk>/', TruckEditView.as_view(), name='edit page'),
    path('details/delete/<int:pk>/', DeleteTruckView.as_view(), name='delete page'),
    path('edit_comment/<int:pk>/', CommentEditView.as_view(), name='edit comment'),
    path('delete_comment/<int:pk>/', CommentDeleteView.as_view(), name='delete comment'),

    path('details/<int:pk>/', details_comment, name='details page'),
    path('details/like/<int:pk>/', like_truck, name='like post'),
]
