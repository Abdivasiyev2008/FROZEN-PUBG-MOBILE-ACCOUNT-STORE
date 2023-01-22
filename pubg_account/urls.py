from django.urls import path
from .views import *

urlpatterns = [
    path('donate/<int:pk>/edit/', DonateAccountUpdateView.as_view(), name='pubg-account-edit'),
    path('donate/<int:pk>/', DonateAccountDetailView.as_view(), name='pubg-account-detail'),
    path('donate/<int:pk>/delete/', DonateAccountDeleteView.as_view(), name='pubg-account-delete'),
    path('donate/new/', DonateAccountCreateView.as_view(), name='pubg-account-new'),
    path('', DonateAccountListView.as_view(), name='pubg-account-list'),

    path('donatsiz/<int:pk>/edit/', DonatesizAccountUpdateView.as_view(), name='pubg-bot-edit'),
    path('donatsiz/<int:pk>/', DonatesizAccountDetailView.as_view(), name='pubg-bot-detail'),
    path('donatsiz/<int:pk>/delete/', DonatesizAccountDeleteView.as_view(), name='pubg-bot-delete'),
    path('donatsiz/new/', DonatesizAccountCreateView.as_view(), name='pubg-bot-new'),
    path('donatsiz/', DonatesizAccountListView.as_view(), name='pubg-bot-list'),
]