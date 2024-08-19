from flet import (UserControl, Text, TextField, Image, ElevatedButton, Column,
                  MaterialState, ButtonStyle, RoundedRectangleBorder, ResponsiveRow, Row,
                  MainAxisAlignment, alignment)

from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewLogin(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.titulo = Text('Login',
                           size=30,
                           color=self.cores.corPrimaria)
        self.imgLogin = Image(src='img_login.png')
        self.t_field_login = TextField(label='Login')
        self.t_field_senha = TextField(label='Senha',
                                       password=True,
                                       can_reveal_password=True)
        self.btn_entrar = ElevatedButton(text='Logar',
                                         expand=True,
                                         style=ButtonStyle(
                                             color=self.cores.corBranca,
                                             bgcolor={
                                                 MaterialState.DEFAULT: self.cores.corDefault,
                                                 MaterialState.HOVERED: self.cores.corHover
                                             },
                                             shape=RoundedRectangleBorder(radius=5),
                                         ))

    def build(self):

        linhaBtnEntrar = Row(col={'xs': 6, 'sm': 4, 'md': 3},
                             controls=[self.btn_entrar])
        linhaImg = Row(controls=[self.imgLogin], alignment=MainAxisAlignment.CENTER)

        layuot = ResponsiveRow(
            controls=[
                Column(col={'xs': 10, 'sm': 8, 'md': 6, 'lg': 5, 'xl': 3},
                       controls=[
                        Column(col={'xs': 6, 'sm': 2, 'md': 1, 'lg': 2, 'xl': 1},
                               controls=[linhaImg],
                               alignment=alignment.center),
                        Column(col={'sm': 12, 'md': 8},
                               controls=[self.titulo,
                                         self.t_field_login,
                                         self.t_field_senha,
                                         linhaBtnEntrar
                                         ])     # fim da coluna de entrada dos botoes

                    ], alignment=MainAxisAlignment.CENTER

                )   # fim da coluna principal

            ], alignment=MainAxisAlignment.CENTER

        )   # fim da linha responsiva

        return layuot
