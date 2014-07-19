from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'SiGeO - UFBA'
settings.subtitle = 'Sistema Geral de Ouvidoria da UFBA'
settings.author = 'CQEN'
settings.author_email = ''
settings.keywords = ''
settings.description = 'Sistema geral de ouvidoria da ufba'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'fc26c5a2-ce5e-4fd4-ba87-0a4a75c758f9'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []

error_m = {
'vazio':'Este campo não pode estar vazio, Por favor preencha este campo',
'imagem':'O arquivo precisa ser uma imagem. Por favor, selecione uma uma imagem válida',
'email':'Insira um e-mail válido'}
