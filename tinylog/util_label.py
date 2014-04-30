#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from django.views.decorators.csrf import csrf_exempt

import json
from datetime import *

from tinylog.models import *
from tinylog.util import *


def get_mnglabel_block():
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

def get_label_form(id = None):
    label = None
    if id != None:
        label = Label.objects.get(id=id)
    
    d = {}
    d['label'] = label
    
    t = get_template('labelform.html')
    c = Context(d)
    h = t.render(c)
    
    return h
    
def get_mnglabel_extral_block():
    
    cnt = get_label_form()
    
    d = {}
    d['dialog_body'] = cnt
    d['dialog_id'] = 'dialog_label'
    d['dialog_title_id'] = 'dialog_label_title'
    d['dialog_body_id'] = 'dialog_label_body'
    
    btn = {}
    btn['id'] = 'dialog_label_save'
    btn['title'] = u'保存'
    
    d['btns'] = [btn]
       
    t = get_template('dialog.html')
    c = Context(d)
    h = t.render(c)
    
    confirm = get_confirm_dialog()
    
    h = h + confirm
    
    return h
    
##################################################################################
#label
def req_label(req, ctx):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
        
    obj = Label.objects.get(id=ctx)
    d = {}
    if obj != None:
        d['id'] = obj.id
        d['name'] = obj.name
        d['desc'] = obj.desc
        
    h = json.dumps(d)
    
    return HttpResponse(h)
    
@csrf_exempt 
def del_label(req):
    try:
        jobj = json.loads(req.body)
        cat = Label.objects.get(id=jobj['id'])
        cat.delete()
        
    except:
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')

@csrf_exempt    
def update_label(req):
    try:
        jobj = json.loads(req.body)
        t = datetime.today()    
        cat = Label.objects.get(id=jobj['id'])
        cat.name = jobj['title']
        cat.desc = jobj['desc']
        cat.update_time = t
        cat.save()
        
    except:
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')
    
@csrf_exempt    
def new_label(req):
    try:
        jobj = json.loads(req.body)
        
        t = datetime.today()    
        cat = Label(name=jobj['title'], desc=jobj['desc'],
                create_time=t, update_time=t)
        cat.save()
        
    except:
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')