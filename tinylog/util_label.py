#coding: utf-8
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *
from tinylog.util import *


def get_mnglabel_block():
    settings = get_settings()
    labels = settings['labels']
        
    l = []
    for label in labels:
        d = {}
        d['label'] = label
        d['label_count'] = label.passage_set.count()
        l = l + [d]
        
    d = {}        
    d['labels'] = l
    t = get_template('mnglabel.html')
    c = Context(d)
    h = t.render(c)

    return h
  