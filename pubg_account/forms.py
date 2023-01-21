from django import forms
from .models import *

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = ('content',)

class PubgAccountForm(forms.ModelForm):
    class Meta:
        model = PubgAccount
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