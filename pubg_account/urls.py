from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/edit/', PubgAccountUpdateView.as_view(), name='pubg-account-edit'),
    path('<int:pk>/', PubgAccountDetailView.as_view(), name='pubg-account-detail'),
    path('<int:pk>/delete/', PubgAccountDeleteView.as_view(), name='pubg-account-delete'),
    path('new/', PubgAccountCreateView.as_view(), name='pubg-account-new'),
    path('', PubgAccountListView.as_view(), name='pubg-account-list'),
]