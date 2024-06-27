import flet as ft


# vou utilizar essa função para criar o layout da pagina
def main(page: ft.Page):
    page.title = "Primeira pagina"
    tf_nome = ft.TextField(label="Digite o seu nome")
    btn_cadastrar = ft.ElevatedButton(text="Cadastrar")

    # page.add tem que vir antes do update
    page.add(tf_nome)
    page.add(btn_cadastrar)

    # criando o evento
    # tem que criar o evento antes de chamar ele
    def enviarNome(e):
        print(tf_nome.value)

    btn_cadastrar.on_click = enviarNome

    # toda vez que eu aletrar a minha pagina, EU DEVO DAR UM UPDATE!!!!!!
    page.update()


if __name__ == '__main__':
    ft.app(main)
