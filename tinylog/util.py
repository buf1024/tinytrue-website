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

def get_settings():
    
    global _g_last_time
    global _g_read_interval
    
    now = int(time())
    diff = now - _g_last_time
    if len(_g_settings) <= 0 or diff >= _g_read_interval:
        _g_last_time = now
        
        settings = Settings.objects.all()
        if len(settings) > 0:
            setting = settings[0]
            modules = Module.objects.filter(visiable=True)
            games = Game.objects.filter(visiable=True)[:setting.game_menu_count]
            passages = Passage.objects.order_by('-front_flag').order_by('-update_date')[:setting.blog_display_count]


            _g_settings['setting'] = setting
            _g_settings['modules'] = modules
            _g_settings['games'] = games
            _g_settings['passages'] = passages

    return _g_settings


def generate_extral_block():
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

def generate_head_nav_block():
    settings = get_settings()
    setting = settings['setting']
    
    games = settings['games']

    d = {}
    
    d['brand'] = setting.brand
    d['games'] = games
    d['admin'] = is_admin()

    t = get_template('header.html')
    c = Context(d)
    h = t.render(c)

    return h;

def generate_passage_block():
    settings = get_settings()
    setting = settings['setting']
    passages = settings['passages']

    h = ''
    t = get_template('passage.html')
    for passage in passages:
        d = {}
        
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
    return False