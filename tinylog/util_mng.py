#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *

def generate_mnggame_block():
    settings = get_settings()
    games = settings['games']
       
    d = {}
    d['games'] = games
    t = get_template('mnggame.html')
    c = Context(d)
    h = t.render(c)

    return h;
    
def generate_mngcatalog_block():
    settings = get_settings()
    pcatalogs = settings['pcatalogs']
    gcatalogs = settings['gcatalogs']
        
    l = []
    for catalog in pcatalogs:
        d = {}
        d['catalog'] = catalog
        d['passage_count'] = catalog.passage_set.count()
        l = l + [d]
    
    for catalog in gcatalogs:
        d = {}
        d['catalog'] = catalog
        d['passage_count'] = catalog.game_set.count()
        l = l + [d]
    d = {}
    d['catalogs'] = l
    t = get_template('mngcatalog.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def generate_mnglabel_block():
    settings = get_settings()
    labels = settings['labels']
        
    l = []
    for label in labels:
        d = {}
        d['label'] = label
        d['label_count'] = label.passage_set.count()
        l = l + [d]
        
    d = {}        
    d['labels'] = l
    t = get_template('mnglabel.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def generate_mngcomment_block():
    settings = get_settings()
    setting = settings['setting']
    comments = Comment.objects.all()[:setting.blog_display_count]
    
        
    d = {}        
    d['comments'] = comments
    d['page_count_block'] = generate_comment_count_block()
    t = get_template('mngcomment.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def generate_mngpassage_block():
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
    d['page_count_block'] = generate_passage_count_block()
    
    t = get_template('mngpassage.html')
    c = Context(d)
    h = t.render(c)

    return h