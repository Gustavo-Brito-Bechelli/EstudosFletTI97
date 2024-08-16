from sistemaBancario.view.viewRelatorio import ViewRelatorio

class ControllerRelatorio:

    def __init__(self, telaRelatorio: ViewRelatorio) -> None:
        self.opcoes = telaRelatorio

    def trocarDePagina(self, e):
        self.opcoes.page.go('/relatorio')
