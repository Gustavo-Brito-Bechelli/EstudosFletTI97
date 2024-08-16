from sistemaBancario.view.viewCadastro import ViewCadastro
from sistemaBancario.controller.controllerCadastrar import ControlerCadastrar


def constructorCadastrar():

    telaCadastrar = ViewCadastro()
    controllerCadastrar = ControlerCadastrar(telaCadastrar)

    return telaCadastrar
