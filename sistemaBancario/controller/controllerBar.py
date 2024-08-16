from sistemaBancario.view.viewBar import ViewBar


class ControllerBarMenu:
    def __init__(self, viewBar: ViewBar) -> None:
        self.barraMenu = viewBar
        self.voltar = viewBar.btn_voltar
        self.btnOperacoes = viewBar.btn_operacoes
        self.btnCadastrar = viewBar.btn_cadastrar
        self.btnRelatorio = viewBar.btn_relatorio
        self.btnOperacoes.on_click = self.trocarDePagina_operacoes
        self.btnCadastrar.on_click = self.trocarDePagina_cadastrar
        self.btnRelatorio.on_click = self.trocarDePagina_relatorio
        self.voltar.on_click = self.voltarPagina

    def trocarDePagina_operacoes(self, e):
        self.barraMenu.page.go('/operacoes')

    def trocarDePagina_cadastrar(self, e):
        self.barraMenu.page.go('/cadastrar')

    def trocarDePagina_relatorio(self, e):
        self.barraMenu.page.go('/relatorio')

    def voltarPagina(self, e):
        self.barraMenu.page.go('/')
