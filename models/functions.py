# coding: utf8
def send_email(nome, email, assunto, mensagem):

    session.name = nome
    session.email = email
    session.subject = assunto
    session.message = mensagem

    if mail:
        if mail.send(to=['contatosigeo@gmail.com'],
            subject=session.subject,
            message= "Email de contato. \n\nNome :"+ session.name+" \nE-mail : " + session.email +"\nMensagem : "+session.message+ ".\n "
        ):
            response.flash = 'Email enviado com sucesso. Aguarde por nosso contato.'
            URL('default','index')
        else:
            response.flash = 'Falha ao enviar email, desculpe'
    else:
        response.flash = 'Incapaz de enviar email : parametros de email não definidos'
