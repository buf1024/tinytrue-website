# coding: utf-8
# Create your views here.
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *
from tinylog.util_mng import *

def home(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_home_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()    
    #文章数据填充
    d['passages_block'] = generate_passage_block()
    #文章数填充
    d['passage_count_block'] = generate_passage_count_block()
    #模块数据填充
    d['bulletins_block'] = generate_bulletins_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('home.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)

def install(req):
    return HttpResponse('not implement')
    
def admin(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_login_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('login.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mngpassage(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
    
    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_login_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('login.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mngcomment(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')
    
    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
        
    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_login_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('login.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
    
def mngcatalog(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
    
    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title + u' : 分类管理'
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #游戏管理
    d['manage_block'] = generate_mngcatalog_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('manage.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mnglabel(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
        
    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_login_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('login.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
    
def mngsetting(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
        
    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_login_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('login.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)
   
def mnggame(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('/install')

    if is_admin() == False:
        return HttpResponseRedirect('/manage/admin')
        
    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title + u' : 游戏管理'
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()
    #游戏管理
    d['manage_block'] = generate_mnggame_block()
    #填充脚注
    d['footer_block'] = generate_footer_block()
        

    t = get_template('manage.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)