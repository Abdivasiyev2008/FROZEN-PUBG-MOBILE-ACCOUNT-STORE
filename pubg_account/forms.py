from django import forms
from .models import *

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = ('content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)


class DonatesizAccountForm(forms.ModelForm):
    class Meta:
        model = DonatesizAccount
        fields = (
        'pubg_id',
        'image',
        'video',
        'kimlar',
        'avtomat',
        'granada',
        'sumka',
        'kaska',
        'parachute',
        'mashina',
        'personaj',
        'emoji',
        'titul',
        'narxi',
        'instagram', 
        'telegram',
    )

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