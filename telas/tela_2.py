from flet import Page, TextField, ElevatedButton, app, Text

# Page = utilizado para criar e configurar a aparencia da pagina/projeto,é nela que trabalhamos as routes de novas Pages

# TextField = camp de entrada de Texto, no qual entramos com dados, podemos configurar diferentes parametros de entrada

# ElevatorButton = é um botão


def main(pagina: Page):

    # Esse parametro terá tudo que uma Page faz e tem
    pagina.title = "Segunda Tela"

    # uzando o window_max quer dizer que voce so pode abrir ate essa medida
    pagina.window_max_width = 600
    pagina.window_max_height = 700

    # largura real dela
    pagina.window_width = 600
    pagina.window_height = 700

    # definindo tamanho minimo da tela
    pagina.window_min_width = 400
    pagina.window_min_height = 500

    # carregamdo pagina/projeto no centro da tela
    pagina.window_center()

    # cor de fundo
    pagina.bgcolor = "#4682B4"

    # incrementando elementos na tela

    # TextField = permirtir pegar dados da tela
    t_field_nome = TextField(label="Digite o seu nome")
    t_field_salario = TextField(label="Digite o seu salario", prefix_text="R$")

    # text = texto que aparece dentro do botao
    btn_calcular = ElevatedButton(text='Calcular')

    # a função tem que ser criada antes do on_click
    def calculando(e):
        # eu posso pegar o valor do TextField utilizando o atributo value
        txt_resposta.value = f"Nome: {t_field_nome.value} tem o salario de R$ {t_field_salario.value}"

        # limpando os campos ja digitados
        t_field_nome.value = ""
        t_field_nome.update()
        t_field_salario.value = ""
        t_field_salario.update()

        txt_resposta.update()

    # todo evento é construido dentro de uma função
    btn_calcular.on_click = calculando

    # value = valor inicial do nosso texto
    # size = modifcar o tamanho do texto
    txt_resposta = Text(value='Resposta', size=20)

    # estou tulizando "add" para adicionar elemtos na minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()


# app = carrega nossa pagina/projeto, responsavel de determinar se vai ser uma aplicação local ou web
app(target=main)
