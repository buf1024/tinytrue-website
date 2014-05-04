#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import *

from tinylog.models import *
from tinylog.util import *

def get_mngpassage_extral_block():
    pass
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
    
def get_mngpassage_newpassage_extral_block():
    pass
    
def get_mngpassage_newpassage_block():
    settings = get_settings()    
    pcatalogs = settings['pcatalogs']
    
    d = {}
    d['passage_visiable'] = True
    d['passage_commentable'] = True
    d['catalogs'] = pcatalogs
    t = get_template('editpassage.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def new_passage(req):
    pass
    
def edit_passage(req):
    pass
    
def del_passage(req):
    pass
    
def backup_passage(req):
    pass
    
def save_passage(req):
    pass