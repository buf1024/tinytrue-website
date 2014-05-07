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
    h = get_confirm_dialog()    
    return h
def get_mngpassage_block():
    settings = get_settings()
    setting = settings['setting']
    passages = Passage.objects.all()
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
    
def get_editpassage_extral_block():
    d = {}
    d['catalog'] = None
    
    t = get_template('catalogform.html')
    c = Context(d)
    h = t.render(c)
    
    d = {}
    d['dialog_body'] = h
    d['dialog_id'] = 'dialog_catalog'
    d['dialog_title_id'] = 'dialog_catalog_title'
    d['dialog_body_id'] = 'dialog_catalog_body'
    
    btn = {}
    btn['id'] = 'dialog_catalog_save'
    btn['title'] = u'保存'
    
    d['btns'] = [btn]
       
    t = get_template('dialog.html')
    c = Context(d)
    h = t.render(c)
    
    return h
    
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
    
def get_mngpassage_modifypassage_block(p):
    h = ''
    try:
        settings = get_settings()    
        pcatalogs = settings['pcatalogs']
        
        d = {}
        d['passage_title'] = p.title
        d['passage_content'] = p.content
        d['catalogs'] = pcatalogs
        d['catalog_selected'] = p.catalog.id
        d['passage_visiable'] = p.visiable
        d['passage_commentable'] = p.enable_comment
        d['passage_front'] = p.front_flag
        d['passage_summary'] = p.summary
        tags = ''
        for tag in p.labels.all():
            if tags == '':
                tags = tag.name
            else:
                tags = tags + ';' + tag.name
        d['passage_tags'] = tags
        d['passage_id'] = p.id
        d['passage_role'] = 'update'
        
        t = get_template('editpassage.html')
        c = Context(d)
        h = t.render(c)

    except Exception, e:
        print e
        t = get_template('404.html')
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
        
        t = datetime.datetime.today()
        
        if role == "update":
            id = jobj['id']            
            p = Passage.objects.get(id=id)
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
                        l = Label(name=tag, desc=tag, create_time=t, update_time=t)
                        l.save()
                    else:
                        l = l[0]
                    p.labels.add(l)
            p.save()
            
        else:
            p = Passage(title = title, content = content, summary=sumary,
                    hot = 0, visiable = visiable, enable_comment = commentable,
                    front_flag = front, draft_flag = isdraft,
                    create_time = t, update_time = t)
            p.catalog = cat
            
            y = t.year
            m = t.month
            
            if m <= 9:
               m = '0' + str(m)
            
            ar = Archive.objects.filter(year=y).filter(month=m)
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
            
        get_settings(True)
    except Exception, e:
        print e
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')
    
@csrf_exempt
def del_passage(req):
    try_redirect()
    try:
        jobj = json.loads(req.body)        
        id = jobj['id']
        p = Passage.objects.get(id=id)
        p.delete()
        get_settings(True)
    except Exception, e:
        print e
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')

@csrf_exempt
def comment_passage(req):
    try:
        jobj = json.loads(req.body)   
        ip = req.META['REMOTE_ADDR']
        id = jobj['id']
        role = jobj['role']
        p = None
        pc = None
        if role == 'p':
            p = Passage.objects.get(id=id)
        else:
            pc = Comment.objects.get(id=id)
            p = pc.passage            
        
        c = Comment()
        c.author = jobj['name']
        c.email = jobj['email']
        c.site = jobj['site']
        c.image = '/img/run.png'
        c.content = jobj['comment']
        c.ip_address = ip
        c.create_time = datetime.datetime.today()
        c.passage = p
        c.parent = pc
        c.save()
    except Exception, e:
        print e
        return HttpResponse('FAIL')

    return HttpResponse('SUCCESS')

    
def backup_passage(req):
    pass
    

def get_cat_passage_block(ctx):
    h = ''
    try:
        cat = Catalog.objects.get(id=ctx)
        passages = cat.passage_set.filter(visiable=True, draft_flag=False)
        d = {}
        d['collect_title'] = u'分类: ' + cat.name
        d['collet_type'] = u'分类'
        dl = []
        for p in passages:
            di = {}
            di['id'] = p.id
            di['cat'] = cat.name
            di['name'] = p.title
            di['hot'] = p.hot
            c = p.comment_set.count()            
            di['comment_count'] = c
            
            dl.append(di)
                    
        d['items'] = dl
        
        t = get_template('collect.html')
        c = Context(d)
        h = t.render(c)
        
    except Exception, e:
        print e
        d = {}
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)
        
    return h
    
def get_label_passage_block(ctx):
    h = ''
    try:
        label = Label.objects.get(id=ctx)
        passages = label.passage_set.filter(visiable=True, draft_flag=False)
        d = {}
        d['collect_title'] = u'标签: ' + label.name
        d['collet_type'] = u'标签'
        dl = []
        for p in passages:
            di = {}
            di['id'] = p.id
            di['cat'] = label.name
            di['name'] = p.title
            di['hot'] = p.hot
            c = p.comment_set.count()           
            di['comment_count'] = c
            dl.append(di)
                    
        d['items'] = dl
        
        t = get_template('collect.html')
        c = Context(d)
        h = t.render(c)
        
    except Exception, e:
        print e
        d = {}
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)
        
    return h
    
def get_ar_passage_block(ctx):
    h = ''
    try:
        y = ctx[:4]
        m = ctx[4:]
        
        ar = Archive.objects.get(year=y, month=m)
        passages = ar.passage_set.filter(visiable=True, draft_flag=False)
        d = {}
        d['collect_title'] = u'归档: ' + ctx
        d['collet_type'] = u'归档日期'
        dl = []
        for p in passages:
            di = {}
            di['id'] = p.id
            di['cat'] = ctx
            di['name'] = p.title
            di['hot'] = p.hot
            c = p.comment_set.count()            
            di['comment_count'] = c
            dl.append(di)
                    
        d['items'] = dl
        
        t = get_template('collect.html')
        c = Context(d)
        h = t.render(c)
        
    except Exception, e:
        print e
        d = {}
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)
        
    return h
    
def get_cat_more_block(): 
    h = ''
    try:
        cats = Catalog.objects.filter(type=1)
        d = {}
        d['collect_title'] = u'分类汇总'
        dl = []
        for cat in cats:
            count = cat.passage_set.filter(visiable=True, draft_flag=False).count()            
            di = {}
            di['id'] = cat.id
            di['name'] = cat.name
            di['desc'] = cat.desc
            di['passage_count'] = count
            di['link'] = '/cat/' + str(cat.id)
            dl.append(di)
            
        d['items'] = dl
        
        t = get_template('collectmore.html')
        c = Context(d)
        h = t.render(c)
        
    except Exception, e:
        print e
        d = {}
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)
        
    return h
    
def get_label_more_block(): 
    h = ''
    try:
        labels = Label.objects.all()
        d = {}
        d['collect_title'] = u'标签汇总'
        dl = []
        for label in labels:
            count = label.passage_set.filter(visiable=True, draft_flag=False).count()            
            di = {}
            di['id'] = label.id
            di['name'] = label.name
            di['desc'] = label.desc
            di['passage_count'] = count
            di['link'] = '/label/' + str(label.id)
            dl.append(di)
            
        d['items'] = dl
        
        t = get_template('collectmore.html')
        c = Context(d)
        h = t.render(c)
        
    except Exception, e:
        print e
        d = {}
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)
        
    return h
    
def get_ar_more_block(): 
    h = ''
    try:
        ars = Archive.objects.all()
        d = {}
        d['collect_title'] = u'归档汇总'
        dl = []
        for ar in ars:
            count = ar.passage_set.filter(visiable=True, draft_flag=False).count()            
            di = {}
            name = ar.year + ar.month
            di['id'] = ar.id
            di['name'] = name
            di['desc'] = name + u' 自动归档文章'
            di['passage_count'] = count
            di['link'] = '/ar/' + name
            dl.append(di)
            
        d['items'] = dl
        
        t = get_template('collectmore.html')
        c = Context(d)
        h = t.render(c)
        
    except Exception, e:
        print e
        d = {}
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)
        
    return h