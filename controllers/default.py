# -*- coding: utf-8 -*-
### required - do no delete

#from gluon.tools import Mail

#mail = Mail()

#mail.settings.server = 'smtp.gmail.com:465'
#mail.settings.sender = 'myemail@gmail.com'
#mail.settings.login = 'myemail@gmail.com:secret'

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def contact():
    form=FORM(TABLE(TR("Seu Nome:",INPUT(_type="text",_name="name",requires=IS_NOT_EMPTY())),
                    TR("Seu Email:",INPUT(_type="text",_name="email",requires=IS_EMAIL())),
                    TR("Mensagem:",TEXTAREA(_name="mensagem")),
                    TR("",INPUT(_type="submit",_value="Enviar"))))
    return dict(form=form, vars=form.vars)

def error():
    return dict()

@auth.requires_login()
def db_sigeo_manage():
    form = SQLFORM.smartgrid(db.t_db_sigeo,onupdate=auth.archive)
    return locals()
