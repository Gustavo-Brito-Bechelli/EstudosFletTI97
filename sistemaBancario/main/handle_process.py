from flet import Page, View
from sistemaBancario.main.constructor.constructorCadastrar import constructorCadastrar
from sistemaBancario.main.constructor.constructorOperacoes import constructorOperacoes
from sistemaBancario.main.constructor.constructorBar import constructorBar
from sistemaBancario.main.constructor.constructorLogin import constructorLogin
from sistemaBancario.main.constructor.constructorRelatorio import contructorRelatorio


def start(page: Page):
    page.title = 'Sistema Bancario'

    def modificarRota(rota):
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    constructorLogin()
                ]
            )
        )

        if page.route == "/cadastrar":
            page.views.append(
                View(
                    route="/cadastrar",
                    controls=[
                        constructorBar(),
                        constructorCadastrar()
                    ], drawer=constructorBar()
                )
            )

        if page.route == "/operacoes":
            page.views.append(
                View(
                    route="/operacoes",
                    controls=[
                        constructorBar(),
                        constructorOperacoes()
                    ], drawer=constructorBar()
                )
            )

        if page.route == "/relatorio":
            page.views.append(
                View(
                    route="/relatorio",
                    controls=[
                        constructorBar(),
                        contructorRelatorio()
                    ], drawer=constructorBar()
                )
            )

        page.update()

    page.on_route_change = modificarRota
    page.go(page.route)

