# pagina burra == nao serve para mais nada a nao ser mostrar a tela

from flet import (UserControl, Image, TextField, ElevatedButton, Row, ResponsiveRow,
                  Column, MainAxisAlignment, Text, FontWeight, icons, ButtonStyle,
                  MaterialState, RoundedRectangleBorder, Container)

from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewCadastro(UserControl):
    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.barraSeparadora = Container(bgcolor=self.cores.corPrimaria, height=20, padding=0, margin=0)
        self.img_cadastro = Image(src='banner - banks.png')
        self.titulo = Text('Cadastrar',
                           size=30,
                           weight=FontWeight.BOLD,
                           color=self.cores.corPrimaria)
        self.t_field_login = TextField(label='Login', icon=icons.LOGIN)
        self.t_field_senha = TextField(label='Senha', password=True, icon=icons.PASSWORD)
        self.t_field_email = TextField(label='E-mail', icon=icons.EMAIL)
        self.t_field_telefone = TextField(label='Telefone', icon=icons.CONTACT_PHONE)
        self.t_field_saldo = TextField(label='Saldo', prefix_text='R$', icon=icons.PAYMENT)
        self.btn_cadastrar = ElevatedButton(text='Cadastrar',
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                },
                                                shape=RoundedRectangleBorder(radius=5),
                                            ))

    def build(self):
        linha1 = ResponsiveRow(controls=[
            Column(controls=[self.img_cadastro], alignment=MainAxisAlignment.CENTER),
            Column(controls=[self.barraSeparadora])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 1

        linhaTitulo = Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER)

        linha2 = ResponsiveRow(controls=[
            Column(col={'xs': 12, 'sm': 10, 'md': 4, "lg": 5}, controls=[self.t_field_login]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, "lg": 5}, controls=[self.t_field_senha]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, "lg": 2}, controls=[self.t_field_saldo]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, "lg": 5}, controls=[self.t_field_email]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, "lg": 5}, controls=[self.t_field_telefone]),

        ], alignment=MainAxisAlignment.SPACE_AROUND)  # final da linha 2

        linha3 = Row(controls=[
            Column(controls=[self.btn_cadastrar])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 3

        return Column(controls=[
            linha1, linhaTitulo, linha2, linha3
        ])
