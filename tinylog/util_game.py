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
    
def get_game_form(): 
    
    d = {}
    
    t = get_template('gameform.html')
    c = Context(d)
    h = t.render(c)
    
    return h
   
def get_mnggame_extral_block():
    
    cnt = get_game_form()
    
    d = {}
    d['dialog_body'] = cnt
    d['dialog_id'] = 'dialog_game'
    d['dialog_title_id'] = 'dialog_game_title'
    d['dialog_body_id'] = 'dialog_game_body'
    
    btn = {}
    btn['id'] = 'dialog_game_save'
    btn['title'] = u'保存'
    
    d['btns'] = [btn]
       
    t = get_template('dialog.html')
    c = Context(d)
    h = t.render(c)
    
    confirm = get_confirm_dialog()
    
    h = h + confirm
    
    return h