#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *


def get_login_extral_block():
    d = {}
    
    d['dialog_title'] = r'错误'
    d['dialog_body'] = r'<h3>邮件或密码为空，请重新输入!</h3>'
    d['dialog_buttongs'] = False

    t = get_template('dialog.html')
    c = Context(d)
    h = t.render(c)

    return h

def get_mnglogin_block():
    d = {}
    t = get_template('login.html')
    c = Context(d)
    h = t.render(c)

    return h
    

    
    