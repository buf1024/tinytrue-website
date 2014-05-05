#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *
from django.db.models import *

from tinylog.models import *

from time import time

# 10分钟
_g_read_interval = 10 * 60
_g_last_time = 0

_g_settings = {}

       
def get_settings(is_force = False):
    
    global _g_last_time
    global _g_read_interval
    
    now = int(time())
    diff = now - _g_last_time
    if len(_g_settings) <= 0 or diff >= _g_read_interval or is_force:
        _g_last_time = now
        
        settings = Settings.objects.all()
        if len(settings) > 0:
            setting = settings[0]
            modules = Module.objects.filter(visiable=True)
            games = Game.objects.filter(visiable=True)[:setting.game_menu_count]
            passages = Passage.objects.order_by('-front_flag', '-update_time')[:setting.blog_display_count]
            pcatalogs = Catalog.objects.filter(type=1).order_by('-update_time')
            gcatalogs = Catalog.objects.filter(type=2).order_by('-update_time')
            labels = Label.objects.all()

            _g_settings['setting'] = setting
            _g_settings['modules'] = modules
            _g_settings['games'] = games
            _g_settings['passages'] = passages
            _g_settings['pcatalogs'] = pcatalogs
            _g_settings['gcatalogs'] = gcatalogs
            _g_settings['labels'] = labels
            
            _g_settings['stdjss'] = ['/js/jquery-2.0.0.min.js', '/js/bootstrap.min.js', '/js/bigfalse.js']
            _g_settings['stdcss'] = ['/css/bootstrap.min.css', '/css/bootstrap-theme.min.css', '/css/bigfalse.css']

    return _g_settings

def get_header_block(webtitle, extjs = None, extcss = None):
    settings = get_settings()
            
    d = {}
    
    d['webtitle'] = webtitle
    
    d['mstdjss'] = settings['stdjss']
    d['mstdcss'] = settings['stdcss']
    
    d['mextjs'] = extjs
    d['mextcss'] = extcss
       
    
    t = get_template('header.html')
    c = Context(d)
    h = t.render(c)
    
    return h
    
def get_home_extral_block():
    settings = get_settings()
    games = settings['games']
    
    h = ''
    
    if len(games) <= 0:    
        d = {}
        d['dialog_title'] = r'游戏'
        d['dialog_body'] = r'<h2>SORRY，由于懒惰，游戏列表为空……</h2>'
        d['dialog_buttongs'] = False

        t = get_template('dialog.html')
        c = Context(d)
        h = t.render(c)

    return h
   
def get_nav_block():
    settings = get_settings()
    setting = settings['setting']
    
    games = settings['games']

    d = {}
    
    d['brand'] = setting.brand
    d['games'] = games
    d['admin'] = is_admin()

    t = get_template('nav.html')
    c = Context(d)
    h = t.render(c)

    return h

def get_passage_block():
    settings = get_settings()
    setting = settings['setting']
    
    passages = Passage.objects.filter(visiable=True, draft_flag=False, delete_flag=False).order_by('-front_flag', '-update_time')[:setting.blog_display_count]
            

    h = ''
    t = get_template('passage.html')
    if len(passages) > 0:
        for p in passages:
            d = {}
            d['has_passage'] = True
            d['passage_id'] = p.id
            d['passage_title'] = p.title
            d['passage_create_time'] = p.create_time
            d['passage_update_time'] = p.update_time
            content = p.content
            if setting.blog_overview:
                content = p.summary
            d['passage_content'] = content
            

            comments = p.comment_set.all()
            count = len(comments)
            for comment in comments:
                count += comment.comment_set.count()
            
            d['passage_comment_count'] = count
            d['passage_catolog'] = p.catalog
                    
        
            labels = p.labels.all()
            d['passage_label_list'] = labels
            
            c = Context(d)        
            h = h + t.render(c) + '\n'
    else:
        d = {}
        d['has_passage'] = False
        c = Context(d)        
        h = h + t.render(c) + '\n'
        
    return h

def get_view_passage_block(ctx):
    h = ''
    d = {}
    try:
        p = Passage.objects.get(id = ctx)
        d['has_passage'] = True
        d['passage_id'] = p.id
        d['passage_title'] = p.title
        d['passage_content'] = p.content
        d['passage_create_time'] = p.create_time
        d['passage_update_time'] = p.update_time

        cc = []
        comments = p.comment_set.all().order_by('-create_time')
        count = len(comments)
        for comment in comments:
            count += comment.comment_set.count()
            d = {}
            d['id'] = comment.id
            d['image'] = comment.image
            d['author'] = comment.author
            d['create_time'] = comment.create_time
            d['content'] = comment.content
            
            scomments = comment.comment_set.objects.all().order_by('create_time')
            ccs = []
            for c in scomments:
                sd = {}
                sd['id'] = c.id
                sd['image'] = c.image
                sd['author'] = c.author
                sd['create_time'] = c.create_time
                sd['content'] = c.content
                ccs.append(sd)
            d['comment_set'] = ccs
            cc.append(d)
        
        d['passage_comment_count'] = count
        d['passage_catolog'] = p.catalog
                
        labels = p.labels.all()
        d['passage_label_list'] = labels
        
        t = get_template('passage.html')
        c = Context(d)        
        h = t.render(c)
        
        d = {}
        d['comments'] = cc
        d['enable_comment'] = p.enable_comment
        pre  = Passage.objects.filter(id = (int(ctx) - 1))
        nxt = Passage.objects.filter(id = (int(ctx) + 1))
        if len(pre) > 0:
            d['pre_passage'] = pre[0]
            d['has_passage'] = True
        if len(nxt) > 0:
            d['nxt_passage'] = nxt[0]
            d['has_passage'] = True
            
            
        h = h + '\n'
        t = get_template('comment.html')
        c = Context(d)        
        h = h + t.render(c)
        
        p.hot = p.hot + 1
        p.save()
        
    except Exception, e:
        print e
        t = get_template('404.html')
        c = Context(d)
        h = t.render(c)       
        
    return h
    
def get_passage_count_block():
    settings = get_settings()
    setting = settings['setting']
    
    passage_count = Passage.objects.count()

    h = ''
    if passage_count > 0:
        d = {}
        
        d['page_count_all'] = passage_count
        d['page_count'] = setting.blog_display_count
        d['data_role'] = 'passage'

        t = get_template('pagecount.html')
        c = Context(d)
        h = t.render(c)

    return h;
    
def get_comment_count_block():
    settings = get_settings()
    setting = settings['setting']
    
    comment_count = Comment.objects.count()

    h = ''
    if comment_count > 0:
        d = {}
        
        d['page_count_all'] = comment_count
        d['page_count'] = setting.blog_display_count
        d['data_role'] = 'comment'

        t = get_template('pagecount.html')
        c = Context(d)
        h = t.render(c)

    return h
    
def get_comment(t, m):
    comments = Comment.objects.all().order_by('-create_time')[:m.display_count]

    d = {}
    d['module'] = m
    cl = []
    for c in comments:
        if c.passage.visiable == False:
            continue
        di = {}
        di['link']  = '/passage/' + str(c.passage.id)
        di['content'] = c.content
        cl.append(di)
    if len(comments) == m.display_count:        
        d['module_more_link'] = '/comment/more' 
        
    d['module_list'] = cl
    d['nocontent'] = u'暂无评论'

    c = Context(d)
    h = t.render(c)
    
    return h
    
def get_hot(t, m):
    passages = Passage.objects.filter(visiable=True).order_by('-hot')[:m.display_count]
     
    d = {}
    d['module'] = m
    pl = []
    for p in passages:
        di = {}
        di['link']  = '/passage/' + str(p.id)
        di['content'] = p.title + '(' + str(p.hot) + ')'        
        pl.append(di)
    
    if len(passages) == m.display_count:        
        d['module_more_link'] = '/hot/more' 
    
    d['module_list'] = pl
    d['nocontent'] = u'暂无文章'

    c = Context(d)
    h = t.render(c)
    
    return h
    
def get_comment_hot(t, m):
    passages = Passage.objects.filter(visiable=True).annotate(num_comments=Count('comment')).order_by('-num_comments')[:m.display_count]
    
    d = {}
    d['module'] = m
    pl = []
    for p in passages:
        di = {}
        di['link']  = '/passage/' + str(p.id)
        c = p.comment_set.count()
        for sc in p.comment_set.all():
            c = c + sc.comment_set.count()
        di['content'] = p.title + '(' + str(c) + ')'        
        pl.append(di)
    if len(passages) == m.display_count:        
        d['module_more_link'] = '/commenthot/more' 
    d['module_list'] = pl
    d['nocontent'] = u'暂无热评文章'

    c = Context(d)
    h = t.render(c)
    
    return h
def get_catalog(t, m):
    catalogs = Catalog.objects.filter(type='1')[:m.display_count]
    
    d = {}
    d['module'] = m
    cl = []
    for c in catalogs:
        di = {}
        di['link']  = '/cat/' + str(c.id)
        di['content'] = c.name     
        cl.append(di)
    if len(catalogs) == m.display_count:        
        d['module_more_link'] = '/cat/more' 
    d['module_list'] = cl
    d['nocontent'] = u'暂无分类'

    c = Context(d)
    h = t.render(c)
    
    return h 
def get_tag(t, m):
    return ''      
def get_archive(t, m):
    archives = Archive.objects.all().order_by('-year').order_by('-month')[:m.display_count]
    
    d = {}
    d['module'] = m 
    al = []
    for a in archives:
        di = {}
        di['link']  = '/ar/' + a.year + a.month
        di['content'] = a.year + '-' + a.month     
        al.append(di)
    if len(archives) == m.display_count:        
        d['module_more_link'] = '/ar/more' 
    d['module_list'] = al
    d['nocontent'] = u'暂无归档'

    c = Context(d)
    h = t.render(c)
    
    return h  

def get_module_map():
    d = {}
    
    d[1] = get_comment
    d[2] = get_hot
    d[3] = get_comment_hot
    d[4] = get_catalog
    d[5] = get_tag
    d[6] = get_archive
    
    return d

def get_bulletins_block():
    settings = get_settings()
    setting = settings['setting']
    
    modules = settings['modules']
    
    m = get_module_map()
    h = ''    
    t = get_template('module.html')
    for module in modules:
        if m.has_key(module.id):
            h = h + m[module.id](t, module)

    return h

def get_footer_block():
    settings = get_settings()

    setting = settings['setting']
    
    d = {}
    d['copy_info'] = setting.copy_info

    t = get_template('footer.html')
    c = Context(d)
    h = t.render(c)

    return h

def get_confirm_dialog():
    
    d = {}
    d['dialog_id'] = 'dialog_confirm'
    d['dialog_title_id'] = 'dialog_confirm_title'
    d['dialog_body_id'] = 'dialog_confirm_body'
    
    d['dialog_title'] = u'确认'
    d['dialog_body'] = u'<h2>操作不可逆，是否确定？</h2>'
    
    btn_no = {}
    btn_no['id'] = 'dialog_confirm_no'
    btn_no['title'] = u'取消'
    
    btn_yes = {}
    btn_yes['id'] = 'dialog_confirm_yes'
    btn_yes['title'] = u'确定'
    
    d['btns'] = [btn_no, btn_yes]

    t = get_template('dialog.html')
    c = Context(d)
    h = t.render(c)

    return h
    
def is_admin():
    return True
    
def try_redirect():    
    settings = get_settings(True);
    if len(settings) == 0:
        return HttpResponseRedirect('/install')
    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')