from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

class DonateAccount(models.Model):

    # Pubg Akkaunt da nimalar bor?
    pubg_id = models.IntegerField()
    rp = models.IntegerField(blank=True, default=0)
    xsuite = models.IntegerField(blank=True, default=0)
    mifik_kiyim = models.IntegerField(blank=True, default=0)
    avtomat = models.IntegerField(blank=True, default=0)
    kill_chat = models.IntegerField(blank=True, default=0)
    granada = models.IntegerField(blank=True, default=0)
    sumka = models.IntegerField(blank=True, default=0)
    kaska = models.IntegerField(blank=True, default=0)
    parachute = models.IntegerField(blank=True, default=0)
    mashina = models.IntegerField(blank=True, default=0)
    samalyot = models.IntegerField(blank=True, default=0)
    vertalyot = models.IntegerField(blank=True, default=0)
    personaj = models.IntegerField(blank=True, default=0)
    emoji = models.IntegerField(blank=True, default=0)
    titul = models.IntegerField(blank=True, default=0)
    hayvon = models.IntegerField(blank=True, default=0)
    narxi = models.FloatField()
    
    # Akkaunt egasi bilan bo'glanish uchun
    instagram = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=30, blank=True)

    # Akkaunt ning rasmi va videosi
    image = models.ImageField(upload_to='pubg_account/images/')
    video = models.FileField(upload_to='pubg_account/videos/')
    
    # Avtomatik vaqtni va post qo'ygan odamni saqlab qoladi
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.pubg_id)
    
    def get_absolute_url(self):
        return reverse('pubg-account-detail', args=[str(self.id)])


class CommentBlog(models.Model):
    blogpost_connected = models.ForeignKey(DonateAccount, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.blogpost_connected} - {self.author}"

class DonatesizAccount(models.Model):
    
    # Pubg Akkaunt da nimalar bor?
    pubg_id = models.IntegerField()
    kimlar = models.IntegerField(blank=True, default=0)
    avtomat = models.IntegerField(blank=True, default=0)
    granada = models.IntegerField(blank=True, default=0)
    sumka = models.IntegerField(blank=True, default=0)
    kaska = models.IntegerField(blank=True, default=0)
    parachute = models.IntegerField(blank=True, default=0)
    mashina = models.IntegerField(blank=True, default=0)
    personaj = models.IntegerField(blank=True, default=0)
    emoji = models.IntegerField(blank=True, default=0)
    titul = models.IntegerField(blank=True, default=0)
    narxi = models.FloatField()
    
    # Akkaunt egasi bilan bo'glanish uchun
    instagram = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=30, blank=True)

    # Akkaunt ning rasmi va videosi
    image = models.ImageField(upload_to='pubg_account/images/')
    video = models.FileField(upload_to='pubg_account/videos/')
    
    # Avtomatik vaqtni va post qo'ygan odamni saqlab qoladi
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.pubg_id)
    
    def get_absolute_url(self):
        return reverse('pubg-bot-detail', args=[str(self.id)])


class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(DonatesizAccount, related_name='donatesiz_comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.blogpost_connected} - {self.author}"
