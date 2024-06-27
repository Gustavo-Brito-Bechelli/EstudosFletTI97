import PySimpleGUI as pg


def layout():
    tela=[
        [pg.Text("Nome")],
        [pg.Input("Digite um nome")],
        [pg.Button("Entrar")],
    ]

    return pg.Window("tela",tela)


layout().read()
