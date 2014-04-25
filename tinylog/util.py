#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *

_g_settings = {}

def get_settings():
    if len(_g_settings) <= 0:
        settings = Settings.objects.all()
        if len(settings) > 0:
            setting = settings[0]
            module = setting.module_set.filter(enable=True)
            games = Game.objects.filter(enable=True)

            _g_settings['setting'] = setting
            _g_settings['module'] = module
            _g_settings['game'] = games

    return _g_settings


def generate_extral_block():
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
    games = settings['game']
    if len(games) > 5:
        games = games[:5]

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

    passages = Passage.objects.order_by('front_weight').order_by('-modified_date')[:setting.display_count]

    h = ''
    t = get_template('passage.html')
    for passage in passages:
        d = {}
        
        d['passage'] = passage

        comments = passage.comment_set.all()
        count = len(comments)
        for comment in comments:
            count += comment.childcomment_set.count()
        d['passage_comment_count'] = count

        cat = passage.catalog_set.count
        if cat > 0:
            d['passage_catolog'] = passage.catalog_set.all()[0].name
        
        d['admin'] = is_admin()

        
        c = Context(d)
    h = t.render(c)

    return h;

def generate_passage_count_block():
    settings = get_settings()

    setting = settings['setting']
    games = settings['game']
    if len(games) > 5:
        games = games[:5]

    d = {}
    
    d['brand'] = setting.brand
    d['games'] = games
    d['admin'] = is_admin()

    t = get_template('header.html')
    c = Context(d)
    h = t.render(c)

    return h;

def generate_bulletins_block():
    settings = get_settings()

    setting = settings['setting']
    games = settings['game']
    if len(games) > 5:
        games = games[:5]

    d = {}
    
    d['brand'] = setting.brand
    d['games'] = games
    d['admin'] = is_admin()

    t = get_template('header.html')
    c = Context(d)
    h = t.render(c)

    return h;

def generate_footer_block():
    settings = get_settings()

    setting = settings['setting']
    
    d['copy_info'] = setting.copy_info

    t = get_template('footer_block.html')
    c = Context(d)
    h = t.render(c)

    return h;

def is_admin():
    return False