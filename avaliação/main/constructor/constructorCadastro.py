from avaliação.view.viewCadastro import ViewCadastro
from avaliação.controller.controllerCadastro import ControllerCadastro


def constructorCadastro():

    telaCadastro = ViewCadastro()
    controllerCadastro = ControllerCadastro(telaCadastro)

    return telaCadastro
