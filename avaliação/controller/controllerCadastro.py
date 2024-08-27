from avaliação.view.viewCadastro import ViewCadastro


class ControllerCadastro:

    def __init__(self, telaCadastro: ViewCadastro):
        self.opcoes = telaCadastro
        self.btn_cadastrar = telaCadastro.btn_cadastrar
        self.t_field_nome = telaCadastro.t_field_nome
        self.t_field_descricao = telaCadastro.t_field_descricao
        self.t_field_preco = telaCadastro.t_field_preco
        self.t_field_data = telaCadastro.t_field_data
        self.t_field_quant = telaCadastro.t_field_quant
        self.btn_cadastrar.on_click = self.escrever

    def escrever(algo: str) -> None:
        arquivo = open('texto.txt', 'a', encoding='utf-8')
        arquivo.write(f'{algo}\n')
        arquivo.close()
