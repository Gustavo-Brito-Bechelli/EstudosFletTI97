from flet import *


def main(page: Page):

    page.title = 'Estudando Cards'

    produto = Card(
        content=Container(      # content == aceita 1 elemento

            content=Column(

                controls=[      # controls == aceita mais de 1 elemento

                    Row(controls=[Image(src="../imagens/pizza.png")],
                        alignment=MainAxisAlignment.CENTER),

                    Row(controls=[Text("Pizza para as noites de Domingo",
                                       color=colors.ORANGE_100,
                                       weight=FontWeight.BOLD)],
                        alignment=MainAxisAlignment.CENTER),

                    Row(controls=[Text("Nenhum pouco apimentado",
                                       color=colors.ORANGE_100,
                                       weight=FontWeight.BOLD)],
                        alignment=MainAxisAlignment.CENTER),

                    Row(controls=[
                        Icon(cupertino_icons.HEART,
                             color=colors.RED),
                        Icon(cupertino_icons.MONEY_DOLLAR,
                             color=colors.GREEN),
                    ],
                        alignment=MainAxisAlignment.SPACE_AROUND),

                ],
            ),
            width=230
        )
    )

    page.add(produto)
    page.update()


if __name__ == '__main__':
    app(main)
