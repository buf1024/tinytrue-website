#!/usr/bin/env python
#coding: utf-8
import os
import sys
import smtplib
from email.mime.text import MIMEText
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tinytrue.settings")

from django.template.loader import *
from django.template import *
from tinylog.models import *


SMTP_HOST = 'smtp.qq.com'
SMTP_PORT = 465

SMTP_USER = '624038220@qq.com'
SMTP_PASS = '=-8/abc123'

SMTP_FROM = '624038220@qq.com'
SMTP_NOTIFY = '450171094@qq.com'

LOOP_PAUSE_TIME = 120

MY_SITE = 'www.bigfalse.com'

def send_mail(comment):    
    try:
        t = get_template('sendmail.html')
        
        tocmmt_email = None
        tocmmt_content = None
        
        d = {}
        if comment.parent != None:
            d['mail_content'] = comment.content
            d['notify_commenter'] = True
            d['ref_content'] = comment.parent.content
            d['comment_link'] = MY_SITE + '/passage/' + str(comment.passage.id) +  '#comment_content_' + str(comment.id)
            d['comment_link_title'] = d['comment_link']   
            c = Context(d)
            tocmmt_content = t.render(c)
            tocmmt_email = comment.parent.email
        
        toau_content = None
        toau_email = SMTP_NOTIFY
        d['mail_content'] = comment.content
        d['notify_commenter'] = False
        d['comment_link'] = MY_SITE + '/passage/' + str(comment.passage.id) +  '#comment_content_' + str(comment.id)
        d['comment_link_title'] = d['comment_link']
        c = Context(d)
        toau_content = t.render(c)
                
        smtp = smtplib.SMTP_SSL(host=SMTP_HOST, port=SMTP_PORT)
        smtp.login(SMTP_USER, SMTP_PASS)
        
        if tocmmt_content != None:
            msg = MIMEText(tocmmt_content, 'html', 'utf-8')        
            msg['Subject'] = u'你的评论有人回复'
            msg['From'] = SMTP_USER
            msg['To'] = tocmmt_email       
            smtp.sendmail(SMTP_FROM, [tocmmt_email], msg.as_string())
        
        if toau_content != None:
            msg = MIMEText(toau_content, 'html', 'utf-8')        
            msg['Subject'] = u'你的文章有人回复'
            msg['From'] = SMTP_USER
            msg['To'] = toau_email       
            smtp.sendmail(SMTP_FROM, [toau_email], msg.as_string())
        
        smtp.quit()
    except Exception, e:
        print e
        return False
        
    return True
        
def main():
    while True:
        comments = Comment.objects.filter(is_notify=False)
        for comment in comments:
            s = send_mail(comment)
            print 'send mail, ret = ' + str(s)
            if s == True:
                comment.is_notify = True
                comment.save()
        print 'sleeping'
        time.sleep(LOOP_PAUSE_TIME)
if __name__ == '__main__':
    main()