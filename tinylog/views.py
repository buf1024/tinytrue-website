# coding: utf-8
# Create your views here.
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *

def home(req):
    settings = get_settings();

    #第一次启动初始化数据
    if len(settings) == 0:
        return HttpResponseRedirect('install')

    d = {}

    setting = settings['setting']
    #title 数据填充
    d['web_title'] = setting.title
    #额外信息填充
    d['extral_block'] = generate_extral_block()
    #导航数据填充
    d['head_nav_block'] = generate_head_nav_block()    
    #文章数据填充
    d['passages_block'] = generate_passage_block()
    #文章数填充
    d['passage_count_block'] = generate_passage_count_block()
    #模块数据填充
    d['bulletins_block'] = generate_footer_block()
    #填充脚注
    d['footer_block'] = 
        

    t = get_template('home.html')
    c = Context(d)
    h = t.render(c)

    return HttpResponse(h)

def install(req):
    return HttpResponse('not implement')
