from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)

class DonateAccountForm(forms.ModelForm):
    class Meta:
        model = DonateAccount
        fields = (
        'pubg_id', 
        'image', 
        'video', 
        'rp', 
        'xsuite', 
        'mifik_kiyim', 
        'avtomat', 
        'kill_chat', 
        'granada',
        'sumka',
        'kaska',
        'parachute',
        'mashina',
        'samalyot',
        'vertalyot',
        'personaj',
        'emoji',
        'titul',
        'hayvon',
        'narxi',
        'instagram', 
        'telegram',
    )