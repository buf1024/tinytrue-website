from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length = 64)
    desc = models.CharField(max_length = 512)
    create_date = models.DateField()
    modified_date = models.DateField()

    def __unicode__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length = 32)
    desc = models.CharField(max_length = 512)
    create_date = models.DateField()
    modified_date = models.DateField()
    
    def __unicode__(self):
        return self.name

class Archive(models.Model):
    year = models.CharField(max_length = 8)
    month = models.CharField(max_length = 4)

    def __unicode__(self):
        return year + '-' + month

class Author(models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField()
    weburl = models.URLField()
    
    def __unicode__(self):
        return self.name

class Passage(models.Model):
    title = models.CharField(max_length = 128)
    content = models.TextField()
    enable_comment = models.BooleanField()
    front_weight = models.IntegerField()

    create_date = models.DateField()
    modified_date = models.DateField()

    catalogs = models.ManyToManyField(Catalog)
    labels = models.ManyToManyField(Label)
    archive = models.ForeignKey(Archive)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.name
        
class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 64)
    email = models.EmailField()
    ip_address = models.IPAddressField()

    passage = models.ForeignKey(Passage)

    def __unicode__(self):
        return self.author
def ChildComment(models.Model):
    child = models.ForeignKey(Comment)

class View(models.Model):
    ip_address = models.IPAddressField()
    view_time = models.DateField()
    passage = models.ForeignKey(Passage)

    def __unicode__(self):
        return self.ip_address

class Settings(models.Model):
    title = models.CharField(max_length = 128)
    brand = models.CharField(max_length = 128)
    display_count = models.IntegerField()
    enable_notify = models.BooleanField()
    display_all = models.BooleanField()
    web_initialize = models.BooleanField()

    copy_info = models.CharField(max_length = 256)

    def __unicode__(self):
        return self.title
        
class Module(models.Model):
    name = models.CharField(max_length = 64)
    title = models.CharField(max_length = 64)
    desc = models.CharField(max_length = 512)
    enable = models.BooleanField()

    setting = models.ForeignKey(Settings)

    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 128)
    email = models.EmailField()

    def __unicode__(self):
        return name


class Game(models.Model):
    name = models.CharField(max_length = 64)
    desc = models.CharField(max_length = 512)
    img = models.CharField(max_length = 128)
    link = models.CharField(max_length = 128)
    enable = models.BooleanField()
    hot = models.IntegerField()

    def __unicode__(self):
        return name
        
        