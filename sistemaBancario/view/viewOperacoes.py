from flet import (UserControl, ElevatedButton, DataTable, DataColumn, Text, Column,
                  Row, ResponsiveRow, MainAxisAlignment, Image, ButtonStyle, MaterialState,
                  RoundedRectangleBorder, FontWeight, TextField)

from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewOperacoes(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        # self.t_field_valor = TextField(label='Valor'),
        self.banner = Image(src='banner - banks.png')
        self.btn_depositar = ElevatedButton(text='Depositar',
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                },
                                                shape=RoundedRectangleBorder(radius=5)
                                            ), width=200, height=45)
        self.btn_sacar = ElevatedButton(text='Sacar',
                                        style=ButtonStyle(
                                            color=self.cores.corBranca,
                                            bgcolor={
                                                MaterialState.DEFAULT: self.cores.corDefault,
                                                MaterialState.HOVERED: self.cores.corHover
                                            },
                                            shape=RoundedRectangleBorder(radius=5)
                                        ), width=200, height=45)
        self.table_operacoes = DataTable(
            columns=[
                DataColumn(Text('Login', color=self.cores.corPrimaria)),
                DataColumn(Text('E-mail', color=self.cores.corPrimaria)),
                DataColumn(Text('Telefone', color=self.cores.corPrimaria)),
                DataColumn(Text('Operação', color=self.cores.corPrimaria)),
                DataColumn(Text('Saldo', color=self.cores.corPrimaria))
            ]
        )

    def build(self):

        linha1 = ResponsiveRow(controls=[
            Column(controls=[self.banner])
        ], alignment=MainAxisAlignment.CENTER)

        linha2 = ResponsiveRow(controls=[
            Column(col={'xs': 3, 'sm': 2, 'md': 4, "lg": 4}, controls=[self.btn_depositar]),
            Column(col={'xs': 3, 'sm': 2, 'md': 4, "lg": 4}, controls=[self.btn_sacar])
        ], alignment=MainAxisAlignment.CENTER)

        linha3 = ResponsiveRow(controls=[
            Column(col={'xs': 5, 'sm': 2, 'md': 6, "lg": 6}, controls=[self.table_operacoes])
        ], alignment=MainAxisAlignment.CENTER)

        return Column(controls=[
            linha1,
            Row(controls=[Text('Operações',
                               color=self.cores.corPrimaria,
                               weight=FontWeight.BOLD,
                               size=30)
                          ], alignment=MainAxisAlignment.CENTER),

            linha2,
            linha3
        ])
