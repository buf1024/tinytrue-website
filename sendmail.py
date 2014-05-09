from django.template.loader import *
from django.template import *

import smtplib
from email.mime.text import MIMEText
from tinylog.models import *

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
            d['comment_link'] = tinytrue.settings.MY_SITE + '/passage/' + str(comment.passage.id) +  '#comment_content_' + str(comment.id)
            d['comment_link_title'] = d['comment_link']   
            c = Context(d)
            tocmmt_content = t.render(c)
            tocmmt_email = comment.parent.email
        
        toau_content = None
        toau_email = tinytrue.settings.SMTP_NOTIFY
        d['mail_content'] = comment.content
        d['notify_commenter'] = False
        d['comment_link'] = tinytrue.settings.MY_SITE + '/passage/' + str(comment.passage.id) +  '#comment_content_' + str(comment.id)
        d['comment_link_title'] = d['comment_link']
        c = Context(d)
        toau_content = t.render(c)
        
        print toau_content
        
        smtp = smtplib.SMTP_SSL(host=tinytrue.settings.SMTP_HOST, port=tinytrue.settings.SMTP_PORT)
        smtp.login(tinytrue.settings.SMTP_USER, tinytrue.settings.SMTP_PASS)
        
        if tocmmt_content != None:
            msg = MIMEText(tocmmt_content, 'html', 'utf-8')        
            msg['Subject'] = u'你的评论有人回复'
            msg['From'] = tinytrue.settings.SMTP_USER
            msg['To'] = tocmmt_email       
            smtp.sendmail(tinytrue.settings.SMTP_FROM, [tocmmt_email], msg.as_string())
        
        if toau_content != None:
            msg = MIMEText(toau_content, 'html', 'utf-8')        
            msg['Subject'] = u'你的文章有人回复'
            msg['From'] = tinytrue.settings.SMTP_USER
            msg['To'] = toau_email       
            smtp.sendmail(tinytrue.settings.SMTP_FROM, [toau_email], msg.as_string())
        
        smtp.quit()
    except Exception, e:
        print e