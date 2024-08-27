from flet import (UserControl, Text, TextField, ElevatedButton, Row, ResponsiveRow, Column,
                  MainAxisAlignment, Image)
from avaliação.utils.paletaDeCores import CoresAplicacao


class ViewLogin(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.banner = Image(src='banner_Golias.png')
        self.titulo = Text(value='Login', size=30, color=self.cores.corPrimaria)
        self.t_field_login = TextField(label='Login')
        self.t_field_senha = TextField(label='Senha',
                                       password=True,
                                       can_reveal_password=True)
        self.btn_entrar = ElevatedButton(text='Entrar')

    def build(self):

        linhaBtnEntrar = Row(controls=[self.btn_entrar], alignment=MainAxisAlignment.CENTER)

        linhaImg = Row(
            controls=[self.banner]
        )

        layout = ResponsiveRow(
            controls=[
                Column(
                    controls=[
                        Column(controls=[linhaImg], alignment=MainAxisAlignment.CENTER),
                        Column(controls=[self.titulo,
                                         self.t_field_login,
                                         self.t_field_senha,
                                         linhaBtnEntrar
                                         ])
                    ], alignment=MainAxisAlignment.CENTER
                )
            ], alignment=MainAxisAlignment.CENTER
        )

        return layout
