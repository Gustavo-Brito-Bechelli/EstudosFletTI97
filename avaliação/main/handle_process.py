from flet import Page, View
from avaliação.main.constructor.constructorLogin import constructorLogin
from avaliação.main.constructor.constructorCadastro import constructorCadastro


def start(page: Page):
    page.title = "Mercadinho do seu Golias"

    def modificarRota(rota):
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    constructorLogin()
                ]
            )
        )

        if page.route == '/cadastrar':
            page.views.append(
                View(
                    route='/cadastrar',
                    controls=[
                        constructorCadastro()
                    ]
                )
            )

        page.update()

    page.on_route_change = modificarRota
    page.go(page.route)

