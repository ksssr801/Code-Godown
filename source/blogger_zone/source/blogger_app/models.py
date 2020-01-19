from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    name = models.CharField(primary_key=True, max_length=500, null=False)
    password = models.CharField(max_length=500, null=False)
    lastupdatetime = models.DateTimeField(auto_now=True)
    creationtime = models.DateTimeField()
    isdeleted = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'tblusers'

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True, db_column='blog_id')
    # user = models.ForeignKey(Users, db_column='name', related_name='blog_user_mapping')
    user = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=500, blank=True)
    blog = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    liked_by = models.TextField(blank=True)
    disliked_by = models.TextField(blank=True)
    commented_by = models.TextField(blank=True)
    viewed_by = models.TextField(blank=True)
    creationtime = models.IntegerField(default=0)
    isdeleted = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'tblblog'
