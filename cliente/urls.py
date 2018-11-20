from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='client_list'),
    path('view/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
    path('new', views.ClientCreate.as_view(), name='client_create'),
    path('edit/<int:pk>', views.ClientUpdate.as_view(), name='client_update'),
    path('delete/<int:pk>', views.ClientDelete.as_view(), name='client_delete'),
]
