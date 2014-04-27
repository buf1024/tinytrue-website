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
        
    d['catalogs'] = l
    t = get_template('mngcatalog.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def generate_mngcatalog_block():
    settings = get_settings()
    label = settings['pcatalogs']
        
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
        
    d['catalogs'] = l
    t = get_template('mngcatalog.html')
    c = Context(d)
    h = t.render(c)

    return h