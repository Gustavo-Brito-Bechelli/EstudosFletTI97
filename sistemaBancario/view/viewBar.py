from flet import (AppBar, Container, IconButton, icons, PopupMenuButton, PopupMenuItem,
                  Image)

from sistemaBancario.utils.paletaCores import CoresAplicacao

# icons.MENU_OUTLINED


class ViewBar(AppBar):
    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.logo = Image(src='finaças logo - modificada.png')
        self.btn_cadastrar = PopupMenuItem(icon=icons.ASSIGNMENT_IND_OUTLINED, text="Cadastrar")
        self.btn_operacoes = PopupMenuItem(icon=icons.PRICE_CHANGE_OUTLINED, text="Operações")
        self.btn_relatorio = PopupMenuItem(icon=icons.AREA_CHART_OUTLINED, text="Relatório")
        self.menu = PopupMenuButton(
            items=[
                self.btn_operacoes,
                self.btn_cadastrar,
                self.btn_relatorio
            ]
        )
        self.btn_voltar = IconButton(icon=icons.LOGOUT,
                                     icon_color=self.cores.corPrimaria)

        self.leading = self.btn_voltar
        self.title = self.logo
        self.center_title = True
        self.actions = [self.menu]
