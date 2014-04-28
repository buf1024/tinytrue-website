#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *

from time import time

# 10分钟
_g_read_interval = 10 * 60
_g_last_time = 0

_g_settings = {}

def get_standard_jss():
    return 

        
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
            passages = Passage.objects.order_by('-front_flag').order_by('-update_date')[:setting.blog_display_count]
            pcatalogs = Catalog.objects.filter(type=1)
            gcatalogs = Catalog.objects.filter(type=2)
            labels = Label.objects.all()

            _g_settings['setting'] = setting
            _g_settings['modules'] = modules
            _g_settings['games'] = games
            _g_settings['passages'] = passages
            _g_settings['pcatalogs'] = pcatalogs
            _g_settings['gcatalogs'] = gcatalogs
            _g_settings['labels'] = labels
            
            _g_settings['standarjs'] = ['/js/jquery-2.0.0.min.js', '/js/bootstrap.min.js', '/js/bigfalse.js']
            _g_settings['standarcss'] = ['/css/bootstrap.min.css', '/css/bootstrap-theme.min.css', '/css/bigfalse.css']

    return _g_settings

def generate_home_extral_block():
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

    return h;

def generate_login_extral_block():
    d = {}
    d['dialog_title'] = r'错误'
    d['dialog_body'] = r'<h3>邮件或密码为空，请重新输入!</h3>'
    d['dialog_buttongs'] = False

    t = get_template('dialog.html')
    c = Context(d)
    h = t.render(c)

    return h;
    
def generate_head_nav_block():
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

    return h;

def generate_passage_block():
    settings = get_settings()
    setting = settings['setting']
    passages = settings['passages']

    h = ''
    t = get_template('passage.html')
    if len(passages) > 0:
        for passage in passages:
            d['has_passage'] = True
            d['passage_id'] = passage.id
            d['passage_title'] = passage.title
            content = passage.content
            if setting.blog_overview:
                content = content[:setting.blog_overview_count]
            d['passage_content'] = content

            comments = passage.comment_set.all()
            count = len(comments)
            for comment in comments:
                count += comment.comment_set.count()
            d['passage_comment_count'] = count

            cats = passage.catalog_set.all()
            if len(cats) > 0:
                d['passage_catolog'] = cats[0].name
                    
        
            labels = passage.label_set.all()
            d['passage_label_list'] = labels
            
            c = Context(d)        
            h = h + t.render(c) + '\n'
    else:
        d = {}
        d['has_passage'] = False
        c = Context(d)        
        h = h + t.render(c) + '\n'
        
    return h;

def generate_passage_count_block():
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
    
def generate_comment_count_block():
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

    return h;
def generate_module(module):
    return ''
    
def generate_bulletins_block():
    settings = get_settings()
    setting = settings['setting']
    
    modules = settings['modules']
    
    h = ''
    for module in modules:
        h = generate_module(module)

    return h;

def generate_footer_block():
    settings = get_settings()

    setting = settings['setting']
    
    d = {}
    d['copy_info'] = setting.copy_info

    t = get_template('footer.html')
    c = Context(d)
    h = t.render(c)

    return h;

def is_admin():
    return True