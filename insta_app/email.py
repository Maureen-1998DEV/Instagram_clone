from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def welcome_email(name,receiver):
    #Creating messwge subject and Sender
    Subject ='welcome To InstaGram'
    sender = 'maureen.ougo@student.moringaschool.com'

    text_content = render_to_string('email/instamail.txt',{"name": name})
    html_content = render_to_string('email/instamail.html',{"name": name})

    msg = EmailMultiAlternatives(Subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()