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
    form=FORM(TABLE(TR("Seu Nome:",INPUT(_type="text",_name="name",requires=IS_NOT_EMPTY(error_message=error_m['vazio']))),
    TR("Seu Email:",INPUT(_type="text",_name="email",requires=IS_EMAIL(error_message=error_m['email']))),
    TR("Assunto:",INPUT(_type="text",_name="assunto",requires=IS_NOT_EMPTY(error_message=error_m['vazio']))),
    TR("Mensagem:",TEXTAREA(_name="mensagem"),requires=IS_NOT_EMPTY(error_message=error_m['vazio'])),
    TR("",INPUT(_type="submit",_value="Enviar"))))
    if form.process().accepted:
        send_email(form.vars.name, form.vars.email, form.vars.assunto, form.vars.mensagem)
    return dict(form=form)


def error():
    return dict()

@auth.requires_login()
def db_sigeo_manage():
    
    db.t_db_sigeo.id.readable=False
    #A linha abaixo ordena conforme a urgencia, para usa-la incluir um parametro no form 'orderby=default_sort_order'
    default_sort_order=[db.t_db_sigeo.f_urgencia]
    form = SQLFORM.smartgrid(db.t_db_sigeo,onupdate=auth.archive, editable=False, deletable=auth.has_membership('delete','db.auth_user'),sortable=True, orderby=default_sort_order,links = [lambda row: A(('Urgencia!'), _href=URL("controllers","urgencia"))])
    return locals()

