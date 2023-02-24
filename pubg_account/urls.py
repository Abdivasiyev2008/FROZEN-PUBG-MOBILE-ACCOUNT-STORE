from django.urls import path
from .views import *

urlpatterns = [
    path('', DonateAccountListView.as_view(), name='pubg-account-list'),
    path('donate/<int:pk>/edit/', DonateAccountUpdateView.as_view(), name='pubg-account-edit'),
    path('donate/<int:pk>/', DonateAccountDetailView.as_view(), name='pubg-account-detail'),
    path('donate/<int:pk>/delete/', DonateAccountDeleteView.as_view(), name='pubg-account-delete'),
    path('donate/new/', DonateAccountCreateView.as_view(), name='pubg-account-new'),

]