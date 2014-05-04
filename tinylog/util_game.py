#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from django.views.decorators.csrf import csrf_exempt

import json
from datetime import *

from tinylog.models import *
from tinylog.util import *

def get_mnggame_block():
    
    games = Game.objects.all()
       
    d = {}
    d['games'] = games
    t = get_template('mnggame.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def get_game_form(): 
    settings = get_settings()
    gcat = settings['gcatalogs']
    
    d = {}
    d['catologs'] = gcat
    
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
    
def req_game(req, ctx):
    try_redirect()        
    obj = Game.objects.get(id=ctx)
    d = {}
    if obj != None:
        d['id'] = obj.id
        d['name'] = obj.name
        d['desc'] = obj.desc
        d['image'] = obj.image
        d['visiable'] = obj.visiable
        
        dcat = {}
        dcat['id'] = obj.catalog.id
        dcat['name'] = obj.catalog.name
        dcat['desc'] = obj.catalog.desc
        
        d['catalog'] = dcat
        
    h = json.dumps(d)
    
    print h
    
    return HttpResponse(h)
    
@csrf_exempt 
def del_game(req):
    try_redirect()
    try:
        jobj = json.loads(req.body)
        game = Game.objects.get(id=jobj['id'])
        game.delete()
        
    except:
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')

@csrf_exempt    
def update_game(req):
    try_redirect()
    try:
        jobj = json.loads(req.body)
        
        t = datetime.today()        
        game = Game.objects.get(id=jobj['id'])
        game.name = jobj['title']
        game.desc = jobj['desc']
        game.image = jobj['image']
        game.visiable = jobj['visiable']
        cat = Catalog.objects.get(id=jobj['catalog']['id'])
        game.catalog = cat
        game.update_time = t
        game.save()
        
    except Exception, e:
        print e
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')
    
@csrf_exempt    
def new_game(req):
    try_redirect()
    try:
        jobj = json.loads(req.body)        
        cat = Catalog.objects.get(id=jobj['catalog']['id'])        
        t = datetime.today()    
        game = Game(name=jobj['title'], desc=jobj['desc'],
                image=jobj['image'], visiable=jobj['visiable'],
                hot=0,
                create_time=t, update_time=t,
                catalog = cat)
        game.save()
        
    except Exception, e:
        print e
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')
    
@csrf_exempt    
def show_game(req):
    try_redirect()
    try:
        jobj = json.loads(req.body)
        
        t = datetime.today()        
        game = Game.objects.get(id=jobj['id'])
        game.visiable = jobj['visiable']
        game.update_time = t
        game.save()
        
    except Exception, e:
        print e
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')