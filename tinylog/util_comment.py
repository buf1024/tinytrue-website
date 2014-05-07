#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *

  
def get_mngcomment_block():
    settings = get_settings()
    setting = settings['setting']
    comments = Comment.objects.all()[:setting.blog_display_count]
 
    d = {}        
    d['comments'] = comments
    d['page_count_block'] = get_comment_count_block()
    t = get_template('mngcomment.html')
    c = Context(d)
    h = t.render(c)

    return h
 