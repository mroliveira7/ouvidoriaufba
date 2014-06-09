### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_db_sigeo',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_assunto', type='string',
          label=T('Assunto')),
    Field('f_local', type='string',
          label=T('Local')),
    Field('f_descricao', type='string',
    	  label=T('Descrição')),
    auth.signature,
    format='%(f_assunto)s',
    migrate=settings.migrate)

db.define_table('t_db_sigeo_archive',db.t_db_sigeo,Field('current_record','reference t_db_sigeo',readable=False,writable=False))