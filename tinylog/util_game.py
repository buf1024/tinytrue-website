#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *

def get_mnggame_block():
    settings = get_settings()
    games = settings['games']
       
    d = {}
    d['games'] = games
    t = get_template('mnggame.html')
    c = Context(d)
    h = t.render(c)

    return h
    
