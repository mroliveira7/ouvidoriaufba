### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_db_sigeo',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_urgencia', type='integer',
          label=T('Urgencia')),
    Field('f_assunto', type='string',
          label=T('Assunto')),
    Field('f_local', type='string',
          label=T('Local')),
    Field('f_descricao', type='string',
    	  label=T('Descrição')),
    Field('f_foto', type='upload',
          label=T('Foto')),
    auth.signature,
    format='%(f_assunto)s',
    migrate=settings.migrate)

db.t_db_sigeo.f_tipo.requires=IS_IN_SET(('Patrimônio danificado','Vandalismo','Incômodo Social'),error_message='Insira um valor válido')
db.t_db_sigeo.f_foto.requires=IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg', 'png', '.gif'),
error_message=error_m['imagem']))
db.t_db_sigeo.f_assunto.requires=IS_NOT_EMPTY(error_message=error_m['vazio'])
db.t_db_sigeo.f_local.requires=IS_NOT_EMPTY(error_message=error_m['vazio'])
db.t_db_sigeo.f_descricao.requires=IS_NOT_EMPTY(error_message=error_m['vazio'])
db.t_db_sigeo.f_urgencia.requires=IS_NOT_EMPTY(error_message=error_m['vazio'])
db.t_db_sigeo.f_urgencia.requires=IS_IN_SET(('1','2','3','4'), error_message='Insira um valor de urgencia')