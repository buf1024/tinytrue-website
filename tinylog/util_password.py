#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import *

from tinylog.models import *

def get_mngpassword_block():    
    d = {}    
    t = get_template('mngpassword.html')
    c = Context(d)
    h = t.render(c)

    return h
    
    
#admin required
@csrf_exempt
def update_password(req):
    r = try_redirect(req)
    if r != None:
        return r
    return HttpResponse('SUCCESS')
    