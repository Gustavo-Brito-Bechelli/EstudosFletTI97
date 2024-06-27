# criar uma aplicação que vai digitar o salario,
# depois vai calcular quanto é 10% desse salario e vai mostrar na tela a resposta.

from flet import Page, TextField, ElevatedButton, app, Text


def main(pagina: Page):
    pagina.title = "Cadastro"
    pagina.bgcolor = "#C0C0C0"

    pagina.window_max_width = 600
    pagina.window_max_height = 700

    pagina.window_width = 600
    pagina.window_height = 700

    pagina.window_min_width = 400
    pagina.window_min_height = 500

    pagina.window_center()
    t_field_nome = TextField(label="Digite o seu nome")
    t_field_salario = TextField(label="Digite o seu salario", prefix_text="R$")

    btn_calcular = ElevatedButton(text='Calcular')

    def calcular(e):
        txt_resposta.value = (f'Nome: {t_field_nome.value}\n'
                              f'Salario: {t_field_salario.value}\n'
                              f'10% do Salario: {float(t_field_salario.value)*0.10}')

        t_field_nome.value = ''
        t_field_nome.update()
        t_field_salario.value = ''
        t_field_salario.update()

        txt_resposta.update()

    btn_calcular.on_click = calcular

    txt_resposta = Text(value='Resposta', size=15)

    pagina.add(t_field_nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()


app(target=main)
