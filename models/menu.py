response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Consultar ou Enviar Irregularidade'),URL('default','db_sigeo_manage')==URL(),URL('default','db_sigeo_manage'),[]),
(T('Contate-nos'),URL('default','contact')==URL(),URL('default','contact'),[])]
