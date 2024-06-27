from flet import *

corlorPrimary = '#728EA6'
secondColor = '#BACDD9'
corBar = '#4C594F'
fontColor = 'ffffff'
backgroundColor = 'ffffff'


def main(pagina: Page):

    pagina.title = "Tela de Inicio"
    pagina.window_min_width = 360
    pagina.window_center()

    pagina.bgcolor = backgroundColor
    imageLogin = Image(src='imagens/Login.png')

    t_field_login = TextField(label='Login', icon=icons.LOGIN_SHARP)
    t_field_passWord = TextField(label='Password', icon=icons.PASSWORD, password=True)

    btn_enter = ElevatedButton(text='Enter',
                               width=300,
                               style=ButtonStyle(
                                   shape=RoundedRectangleBorder(radius=0),
                                   bgcolor={
                                       MaterialState.DEFAULT: corlorPrimary,
                                       MaterialState.HOVERED: secondColor
                                   },
                                   color=fontColor

                               )

                               )

    lineImg = Row(controls=[imageLogin], alignment=MainAxisAlignment.CENTER)
    line1 = Row(controls=[t_field_login], alignment=MainAxisAlignment.CENTER)
    line2 = Row(controls=[t_field_passWord], alignment=MainAxisAlignment.CENTER)
    line3 = Row(controls=[btn_enter], alignment=MainAxisAlignment.CENTER)

    # controls do columns tem que ser uma lista
    coluna = Column(controls=[lineImg, line1, line2, line3])

    # controls == permite que eu trabalhe com mais de um cointainer
    # pagina.add(t_field_login, t_field_passWord, btn_enter)

    pagina.add(coluna)
    pagina.update()


if __name__ == '__main__':
    app(target=main)
