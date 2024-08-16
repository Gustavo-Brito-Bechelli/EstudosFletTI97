from flet import (UserControl, Image, Text, FontWeight, Row, ResponsiveRow,
                  Column, MainAxisAlignment)

from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewRelatorio(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.banner = Image(src='banner - banks.png')
        self.titulo = Text('Relatorio',
                           size=30,
                           weight=FontWeight.BOLD,
                           color=self.cores.corPrimaria)

    def build(self):
        linha1 = ResponsiveRow(controls=[
            Column(controls=[self.banner])
        ], alignment=MainAxisAlignment.CENTER)

        linhaTitulo = Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER)

        return Column(controls=[
            linha1, linhaTitulo
        ])
