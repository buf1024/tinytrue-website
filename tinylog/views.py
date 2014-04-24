# coding: utf-8
# Create your views here.
from django.template.loader import *
from django.template import *
from django.http import *

from tinylog.models import *

def home(req):
	settings = Settings.objects.all();

	#第一次启动初始化数据
	if len(settings) == 0:
		return HttpResponseRedirect('install')

	setting = settings[0]

	d = {}

	#brand title 数据填充
	d['web_title'] = setting.title
	d['brand'] = setting.brand

	games = Game.objects.all();

    #导航数据填充
	d['games'] = games
	d['admin'] = False

	#文章数据填充
	passages = Passage.objects.order_by('front_weight').order_by('-create_date').all()[:setting.display_count]
	for pasage in passages:
		pass
		

	t = get_template('home.html')
	html = t.render(Context(d))
	return HttpResponse(html)

def install(req):
	return HttpResponse('not implement')
