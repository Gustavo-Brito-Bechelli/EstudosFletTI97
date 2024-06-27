from flet import *

corPrimaria = '#2D3740'
corSecundaria = '#4F638C'
btnColor = '#B0BFBE'
backgroundCor = '#D7E9FF'


def main(page: Page):

    page.title = 'Inicio'
    page.window_max_width = 600
    page.window_max_height = 700

    page.window_width = 600
    page.window_height = 700

    page.window_min_width = 360
    page.window_min_height = 500
    page.window_center()

    page.bgcolor = backgroundCor
    imagemLogin = Image(src='../imagens/Login2.png')
    imagemGmail = Image(src='../imagens/mail.png')
    imagemFaceBook = Image(src='../imagens/facebook.png')

    t_field_login = TextField(label='Login', icon=icons.LOGIN)
    t_field_senha = TextField(label='Senha', icon=icons.PASSWORD, password=True)
    t_field_esqueciSenha = TextButton(text='Esqueci a senha')

    btn_entrar = ElevatedButton(text='Entar',
                                width=200,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=5),
                                    bgcolor={
                                        MaterialState.DEFAULT: corPrimaria,
                                        MaterialState.HOVERED: corSecundaria
                                    }
                                ),
                                color=btnColor,
                                icon=icons.TRANSIT_ENTEREXIT
                                )

    linhaImg = Row(controls=[imagemLogin], alignment=MainAxisAlignment.CENTER)
    linha1 = Row(controls=[t_field_login], alignment=MainAxisAlignment.CENTER)
    linha2 = Row(controls=[t_field_senha], alignment=MainAxisAlignment.CENTER)
    linha3 = Row(controls=[btn_entrar], alignment=MainAxisAlignment.CENTER)
    linha4 = Row(controls=[t_field_esqueciSenha], alignment=MainAxisAlignment.CENTER)
    linha5 = Row(controls=[imagemGmail, imagemFaceBook], alignment=MainAxisAlignment.CENTER)

    coluna = Column(controls=[linhaImg, linha1, linha2, linha3, linha4, linha5])
    page.add(coluna)
    page.update()


if __name__ == '__main__':
    app(target=main)
