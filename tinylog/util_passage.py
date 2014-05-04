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
    setting = settings['setting']
    
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
    d['passage_role'] = 'new'
    
    t = get_template('editpassage.html')
    c = Context(d)
    h = t.render(c)

    return h
    
@csrf_exempt 
def edit_passage(req):
    try_redirect()
    try:
        jobj = json.loads(req.body)
        
        title = jobj['title']
        content = jobj['content']
        sumary = jobj['sumary']
        cat = Catalog.objects.filter(id=jobj['catalog'])[0]
        visiable = jobj['visiable']
        front = jobj['front']
        commentable = jobj['commentable']
        isdraft = jobj['isdraft']
        tags = jobj['tags'].split(';')
        
        role = jobj['role']
        
        t = datetime.today()
        
        if role == "update":
            id = jobj['id']            
            p = Passage.objects.filter(id=id)
            p.title = title
            p.content = content
            p.summary = sumary
            p.visiable = visiable
            p.enable_comment = commentable
            p.front_flag = front
            p.draft_flag = isdraft
            p.update_time = t
            
            p.catalog = cat
            p.labels.clear()
            
            for tag in tags:
                if len(tag) > 0:
                    l = Label.objects.filter(name=tag)
                    if len(l) == 0:
                        l = Label(name=tag, desc=tag)
                        l.save()
                    else:
                        l = l[0]
                    p.labels.add(l)
            p.save()
            
        else:
            p = Passage(title = title, content = content, summary=sumary,
                    hot = 0, visiable = visiable, enable_comment = commentable,
                    front_flag = front, draft_flag = isdraft, delete_flag = False,
                    create_time = t, update_time = t)
            p.catalog = cat
            
            y = t.year
            m = t.month
            
            ar = Archive.objects.filter(id=y).filter(month=m)
            if len(ar) == 0:
                ar = Archive(year=y, month=m)
                ar.save()
            else:
                ar = ar[0]
            p.archive = ar
            
            p.save()
            for tag in tags:
                if len(tag) > 0:
                    l = Label.objects.filter(name=tag)
                    if len(l) == 0:
                        l = Label(name=tag, desc=tag, create_time=t, update_time = t)
                        l.save()
                    else:
                        l = l[0]
                    p.labels.add(l)
            
            p.save()
    except Exception, e:
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')
    
def del_passage(req):
    pass
    
def backup_passage(req):
    pass
    
def save_passage(req):
    pass
    
    
    
def cat_passage(req, ctx):
    pass
    
def label_passage(req, ctx):
    pass
    
def view_passage(req, ctx):
    pass