# -*- coding: utf-8 -*-
### required - do no delete

from gluon.tools import Mail


def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def contact():
    form=FORM(TABLE(TR("Seu Nome:",INPUT(_type="text",_name="name",requires=IS_NOT_EMPTY())),
    TR("Seu Email:",INPUT(_type="text",_name="email",requires=IS_EMAIL())),
    TR("Assunto:",INPUT(_type="text",_name="assunto",requires=IS_NOT_EMPTY())),
    TR("Mensagem:",TEXTAREA(_name="mensagem"),requires=IS_NOT_EMPTY()),
    TR("",INPUT(_type="submit",_value="Enviar"))))
    if form.process().accepted:
        send_email(form.vars.name, form.vars.email, form.vars.assunto, form.vars.mensagem)
    return dict(form=form)


def error():
    return dict()

@auth.requires_login()
def db_sigeo_manage():
    form = SQLFORM.smartgrid(db.t_db_sigeo,onupdate=auth.archive)
    return locals()
