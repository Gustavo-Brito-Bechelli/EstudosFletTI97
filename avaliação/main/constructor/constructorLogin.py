from avaliação.view.viewLogin import ViewLogin
from avaliação.controller.controllerLogin import ControllerLogin


def constructorLogin():

    telaLogin = ViewLogin()
    controllerLogin = ControllerLogin(telaLogin)

    return telaLogin
