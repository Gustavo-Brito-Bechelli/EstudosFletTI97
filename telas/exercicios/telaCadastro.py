from flet import *

corlorPrimary = '#232625'
secondColor = '#35403A'
corBar = '#4C594F'
fontColor = 'ffffff'
backgroundColor = 'ffffff'


def main(pagina: Page):

    pagina.title = "Tela de Inicio"
    pagina.bgcolor = corlorPrimary

    pagina.window_max_width = 600
    pagina.window_max_height = 700

    pagina.window_width = 600
    pagina.window_height = 700

    pagina.window_min_width = 400
    pagina.window_min_height = 500

    pagina.window_center()

    t_field_login = TextField(label='Login', icon=icons.LOGIN_SHARP)
    t_field_passWord = TextField(label='Password', icon=icons.PASSWORD, password=True)

    btn_enter = ElevatedButton(text='Enter')

    def cadastro(e):
        txt_resposta.value = (f'Nome: {t_field_login.value}\n'
                              f'Senha: {t_field_passWord.value}')

        t_field_login.value = ''
        t_field_login.update()
        t_field_passWord.value = ''
        t_field_passWord.update()

        txt_resposta.update()

    btn_enter.on_click = cadastro
    txt_resposta = Text(value='Cadastrar', size=15)

    pagina.add(t_field_login)
    pagina.add(t_field_passWord)
    pagina.add(btn_enter)
    pagina.add(txt_resposta)

    pagina.update()


if __name__ == '__main__':
    app(target=main)
