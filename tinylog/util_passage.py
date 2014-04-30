#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *

def get_mngpassage_block():
    settings = get_settings()
    
    passages = settings['passages']
    
    l = []
    for passage in passages:
        d = {}
        d['passage'] = passage
        d['comment_count'] = passage.comment_set.count()
        l = l + [d]
        
    d = {}        
    d['passages'] = l
    d['page_count_block'] = get_passage_count_block()
    
    t = get_template('mngpassage.html')
    c = Context(d)
    h = t.render(c)

    return h