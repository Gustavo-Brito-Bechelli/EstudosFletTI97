from flet import *


def main(page: Page):

    page.title = 'KFC'

    gridview = GridView(
        expand=1,
        runs_count=1,
        max_extent=350,
        child_aspect_ratio=1.0,
        spacing=0,
        run_spacing=5,
    )

    for i in range(1):
        gridview.controls.append(
            Container(
                bgcolor=colors.WHITE30,
                width=200,
                height=200,

                content=Column(

                    controls=[
                        Row(controls=[
                            Image(src='')
                        ], alignment=MainAxisAlignment.CENTER),

                        Row(controls=[Text(value='Pedido',
                                           size=20,
                                           color=colors.BLACK,
                                           weight=FontWeight.BOLD)
                                      ], alignment=MainAxisAlignment.CENTER
                            ),

                        Row(controls=[
                            Column(controls=[

                                Row(controls=[
                                    Icon(icons.CIRCLE,
                                         color=colors.GREEN,
                                         size=8),
                                    Text(value='Lanche',
                                         size=10)
                                    ])
                            ])
                        ])
                    ]
                )   # fim do colunm
            )   # fim do container
        )   # fim da gridview

    page.add(gridview)

    page.update()


if __name__ == '__main__':
    app(main)
