#coding: utf-8

from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length = 64)
    desc = models.CharField(max_length = 512)
    
    #1 ²©¿Í 2 ÓÎÏ·
    type = models.IntegerField()
    
    create_date = models.DateField()
    update_date = models.DateField()

    def __unicode__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length = 32)
    desc = models.CharField(max_length = 512)
    
    create_date = models.DateField()
    update_date = models.DateField()
    
    def __unicode__(self):
        return self.name

class Archive(models.Model):
    year = models.CharField(max_length = 8)
    month = models.CharField(max_length = 4)

    def __unicode__(self):
        return self.year + '-' + self.month

class Author(models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField()
    web_url = models.URLField()
    
    create_date = models.DateField()
    update_date = models.DateField()
    
    def __unicode__(self):
        return self.name

class Passage(models.Model):
    title = models.CharField(max_length = 128)
    content = models.TextField()
    enable_comment = models.BooleanField()
    front_flag = models.BooleanField()

    create_date = models.DateField()
    update_date = models.DateField()

    catalog = models.ForeignKey(Catalog)
    labels = models.ManyToManyField(Label)
    archive = models.ForeignKey(Archive)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.title
        
class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 64)
    email = models.EmailField()
    ip_address = models.IPAddressField()
    visiable = models.IPAddressField()
    
    create_date = models.DateField()
    
    passage = models.ForeignKey(Passage)
    parent = models.ForeignKey('self')

    def __unicode__(self):
        return self.author

class Settings(models.Model):
    title = models.CharField(max_length = 128)
    brand = models.CharField(max_length = 128)
    copy_info = models.CharField(max_length = 256)
    
    #blog setting
    blog_display_count = models.IntegerField()
    blog_notify = models.BooleanField()
    blog_overview = models.BooleanField()
    blog_overview_count = models.IntegerField()
  
    #game setting
    game_menu_count = models.IntegerField()


    def __unicode__(self):
        return self.title
        
class Module(models.Model):
    name = models.CharField(max_length = 64)
    title = models.CharField(max_length = 64)
    desc = models.CharField(max_length = 512)
    
    #setting
    visiable = models.BooleanField()
    display_count = models.IntegerField()
    
    create_date = models.DateField()
    update_date = models.DateField()

    setting = models.ForeignKey(Settings)

    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 128)
    email = models.EmailField()
    
    create_date = models.DateField()
    update_date = models.DateField()
    
    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length = 64)
    desc = models.CharField(max_length = 512)
    image = models.CharField(max_length = 128)
    visiable = models.BooleanField()
    
    catalog = models.ForeignKey(Catalog)
    
    #statistic
    hot = models.IntegerField()

    def __unicode__(self):
        return name
        
        