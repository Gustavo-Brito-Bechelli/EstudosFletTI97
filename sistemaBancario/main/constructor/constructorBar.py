from sistemaBancario.view.viewBar import ViewBar
from sistemaBancario.controller.controllerBar import ControllerBarMenu


def constructorBar():

    barraOpcoes = ViewBar()
    controllerBar = ControllerBarMenu(barraOpcoes)

    return barraOpcoes
