from django.urls import path

from truck_app.views import index, create, details_comment, edit, like_truck, delete, edit_comment, delete_comment

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create, name='create page'),
    path('details/<int:pk>/', details_comment, name='details page'),
    path('edit_comment/<int:pk>/', edit_comment, name='edit comment'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete comment'),
    path('details/like/<int:pk>/', like_truck, name='like post'),
    path('details/edit/<int:pk>/', edit, name='edit page'),
    path('details/delete/<int:pk>/', delete, name='delete page'),
]
