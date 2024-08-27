from avaliação.view.viewLogin import ViewLogin


class ControllerLogin:

    def __init__(self, telaLogin: ViewLogin) -> None:
        self.opcoes = telaLogin
        self.telaLogin = telaLogin
        self.t_field_login = telaLogin.t_field_login
        self.t_field_senha = telaLogin.t_field_senha
        self.btn_entrar = telaLogin.btn_entrar
        self.btn_entrar.on_click = self.logar
        self.btn_entrar.on_click = self.trocarDePagina

    def logar(self, e):
        cadastrados = {
            "login": ['ana', 'caroll', 'rian'],
            "senha": ['23@1', '9669', '6666']
        }

        for ind, login in enumerate(cadastrados["login"]):
            if self.t_field_login.value == login:
                self.t_field_login.error_text = ''
                self.t_field_login.update()

                for j, senha in enumerate(cadastrados["senha"]):
                    if (self.t_field_senha.value == senha) and j == ind:
                        self.telaLogin.page.go('/cadastrar')

                    else:
                        self.t_field_senha.error_text = "Senha invalida !"
                        self.t_field_senha.update()

            else:
                self.t_field_login.error_text = "Login invalido !"
                self.t_field_login.update()

    def trocarDePagina(self, e):
        self.opcoes.page.go('/cadastrar')
