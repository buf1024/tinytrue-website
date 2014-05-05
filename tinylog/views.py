# coding: utf-8
# Create your views here.
from django.template.loader import *
from django.template import *
from django.http import *


from tinylog.models import *
from tinylog.util import *

from tinylog.util_login import *
from tinylog.util_game import *
from tinylog.util_catalog import *
from tinylog.util_label import *
from tinylog.util_comment import *
from tinylog.util_setting import *
from tinylog.util_passage import *

def home(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']
    
    d = {}    
    d['header_block'] = get_header_block(setting.title)    
    d['extral_block'] = get_home_extral_block()    
    d['nav_block'] = get_nav_block()    
    d['passages_block'] = get_passage_block()    
    d['passage_count_block'] = get_passage_count_block()    
    d['bulletins_block'] = get_bulletins_block()    
    d['footer_block'] = get_footer_block()        

    t = get_template('home.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)

def install(req):
    return HttpResponse('not implement')
    
def admin(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}    
    d['header_block'] = get_header_block(setting.title + u' : 登录')    
    d['extral_block'] = get_login_extral_block()    
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mnglogin_block()    
    d['footer_block'] = get_footer_block()        

    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mngpassage(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}
    d['extral_block'] = get_mngpassage_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 文章管理',
                                              extjs = ['/js/mngpassage.js'])    
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mngpassage_block()
    d['footer_block'] = get_footer_block()
    
    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mngpassage_newpassage(req):
    try_redirect()
        
    settings = get_settings()
    setting = settings['setting']

    d = {}
    d['extral_block'] = get_mngpassage_newpassage_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 新增文章',
                                              extjs = ['/tinymce/tinymce.min.js',
                                                '/js/editpassage.js'])    
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mngpassage_newpassage_block()
    d['footer_block'] = get_footer_block()
    
    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
def mngpassage_modifypassage(req, ctx):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']
    
    p = Passage.objects.get(id=ctx)
    
    d = {}
    d['extral_block'] = get_mngpassage_modifypassage_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 修改文章',
                                              extjs = ['/tinymce/tinymce.min.js',
                                                '/js/editpassage.js'])    
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mngpassage_modifypassage_block(p)
    d['footer_block'] = get_footer_block()
    
    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)        
    
    return HttpResponse(h)
def mngcomment(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}   
    d['header_block'] = get_header_block(setting.title + u' : 评论管理')    
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mngcomment_block()    
    d['footer_block'] = get_footer_block()        

    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
    
def mngcatalog(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}
    d['extral_block'] = get_mngcatalog_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 分类管理',
                                              extjs = ['/js/mngcatalog.js'])
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mngcatalog_block()
    d['footer_block'] = get_footer_block()
        

    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mnglabel(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}    
    d['extral_block'] = get_mnglabel_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 标签管理',
                                              extjs = ['/js/mnglabel.js'])    
    d['nav_block'] = get_nav_block()    
    d['content_block'] = get_mnglabel_block()    
    d['footer_block'] = get_footer_block()
        

    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mngsetting(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}        
    d['extral_block'] = get_mngsetting_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 博客设置',
                                             extjs = ['/js/mngsetting.js'])    
    d['nav_block'] = get_nav_block()    
    d['content_block'] = get_mngsetting_block()    
    d['footer_block'] = get_footer_block()        

    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
   
def mnggame(req):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']

    d = {}    
    d['extral_block'] = get_mnggame_extral_block()
    d['header_block'] = get_header_block(setting.title + u' : 游戏管理',
                                             extjs = ['/js/mnggame.js'])    
    d['nav_block'] = get_nav_block()
    d['content_block'] = get_mnggame_block()    
    d['footer_block'] = get_footer_block()
        

    t = get_template('general.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
       
       
   
def cat_passage(req, ctx):
    pass
    
def label_passage(req, ctx):
    pass
    
def view_passage(req, ctx):
    try_redirect()
    
    settings = get_settings()
    setting = settings['setting']
    
    d = {}    
    d['header_block'] = get_header_block(setting.title)    
    d['extral_block'] = get_home_extral_block()    
    d['nav_block'] = get_nav_block()    
    d['passages_block'] = get_view_passage_block(ctx)    
    d['passage_count_block'] = ''   
    d['bulletins_block'] = get_bulletins_block()    
    d['footer_block'] = get_footer_block()        

    t = get_template('home.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)