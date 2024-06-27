# criar uma aplicação que vai pegar o endereço(rua, numero, bairro, cep) da pessoa,
# depois vai mostrar na tela em dois elementos Text.
# EXEMPLO -
# Nome: Carlos
# Endereço: Rua xxxxxx Numero yyyyyy CEP: 00000-000

from flet import Page, TextField, ElevatedButton, app, Text


def main(pagina: Page):

    pagina.title = "Cadastro"
    pagina.bgcolor = "#B0C4DE"

    pagina.window_max_width = 600
    pagina.window_max_height = 700

    pagina.window_width = 600
    pagina.window_height = 700

    pagina.window_min_width = 400
    pagina.window_min_height = 500

    pagina.window_center()

    t_field_nome = TextField(label="Digite o seu nome")
    t_field_rua = TextField(label='Endereço: Rua')
    t_field_numero = TextField(label='Numero: ', prefix_text="N°")
    t_field_bairro = TextField(label='Endereço: Bairro')
    t_field_cep = TextField(label='Endereço: CEP')

    btn_registro = ElevatedButton(text='Reistro')

    def registro(e):
        txt_resposta.value = f"Nome: {t_field_nome.value}"
        txt_resposta2.value = (f'Endereço: Rua {t_field_rua.value}, N°{t_field_numero.value}, '
                               f'{t_field_bairro.value}, CEP: {t_field_cep.value}')

        t_field_nome.value = ""
        t_field_nome.update()
        t_field_rua.value = ""
        t_field_rua.update()
        t_field_numero.value = ""
        t_field_numero.update()
        t_field_bairro.value = ""
        t_field_bairro.update()
        t_field_cep.value = ""
        t_field_cep.update()

        txt_resposta.update()
        txt_resposta2.update()

    btn_registro.on_click = registro

    txt_resposta = Text(value='Resposta', size=20)
    txt_resposta2 = Text(value='Resposta', size=20)

    pagina.add(t_field_nome)
    pagina.add(t_field_rua)
    pagina.add(t_field_numero)
    pagina.add(t_field_bairro)
    pagina.add(t_field_cep)
    pagina.add(btn_registro)
    pagina.add(txt_resposta)
    pagina.add(txt_resposta2)

    pagina.update()


app(target=main)
