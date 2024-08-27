from flet import (UserControl, Text, TextField, ElevatedButton, Row, ResponsiveRow, Column,
                  MainAxisAlignment, Image)
from avaliação.utils.paletaDeCores import CoresAplicacao


class ViewCadastro(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.titulo = Text(value='Cadastrar Produto', size=30, color=self.cores.corPrimaria)
        self.banner = Image(src='banner_Golias.png')
        self.t_field_nome = TextField(label='Nome')
        self.t_field_descricao = TextField(label='Descrição')
        self.t_field_preco = TextField(label='Preço', prefix_text='R$')
        self.t_field_data = TextField(label='Data de Validade')
        self.t_field_quant = TextField(label='Quantidade')
        self.btn_cadastrar = ElevatedButton(text='Cadastrar')

    def build(self):

        linhaBtnCadastrar = Row(
            controls=[self.btn_cadastrar], alignment=MainAxisAlignment.CENTER
        )

        linhaImg = Row(
            controls=[self.banner]
                       )

        layout = ResponsiveRow(
            controls=[
                Column(
                    controls=[
                        Column(controls=[linhaImg], alignment=MainAxisAlignment.CENTER),
                        Column(col={'sm': 12, 'md': 8},
                               controls=[self.titulo,
                                         self.t_field_nome,
                                         self.t_field_descricao,
                                         self.t_field_preco,
                                         self.t_field_data,
                                         self.t_field_quant,
                                         linhaBtnCadastrar
                                         ])
                    ], alignment=MainAxisAlignment.CENTER
                )
            ], alignment=MainAxisAlignment.CENTER
        )

        return layout
