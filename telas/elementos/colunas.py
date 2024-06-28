# Estudando colunas
# A control tat display its children in a vertical array


from flet import *


def main(page: Page):

    page.title = 'Coluna'

    page.on_scroll = True

    listview = ListView(expand=1,
                        spacing=10,
                        padding=20,
                        auto_scroll=True
                        )

    gridview = GridView(
        expand=1,
        runs_count=1,
        max_extent=350,
        child_aspect_ratio=1.0,
        spacing=0,
        run_spacing=5,
    )

    # coluna = Column(spacing=10)
    # for i in range(10):
    #     coluna.controls.append(
    #         Container(content=Text(f"Texto {i}",
    #                                color=colors.BLACK),
    #                   width=200,
    #                   height=200,
    #                   bgcolor=colors.INDIGO_100,
    #                   shadow=BoxShadow(
    #                       spread_radius=20,
    #                       blur_radius=20,
    #                       color=colors.BLUE_GREY_300
    #                   ),
    #                   alignment=Alignment(0, 0),
    #                   border_radius=border_radius.all(5)
    #                   )
    #     )

    # page.add(coluna)

    for i in range(1):
        gridview.controls.append(
            Container(
                bgcolor=colors.GREY_800,
                # width=200,
                # height=350,

                content=Column(

                    controls=[

                        Row(controls=[Image(src='pizza2.png')],
                            alignment=MainAxisAlignment.CENTER),

                        # linha de titulo
                        Row(controls=[
                            Text("Titulo",
                                 size=20,
                                 color=colors.BLACK,
                                 weight=FontWeight.BOLD)
                                      ],
                            alignment=MainAxisAlignment.CENTER),

                        # 1° linha de conteudo
                        Row(controls=[
                            Column(
                                controls=[
                                    Text(f'Loja {i}',
                                         size=13),

                                    Text(f'Lanches',
                                         size=10,
                                         color=colors.GREY_50),

                                    Row(
                                        controls=[Icon(icons.CIRCLE,
                                                       color=colors.GREEN,
                                                       size=13),
                                                  Text('Aberto',
                                                       size=15)
                                                  ]
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER),

                            # 2° linha de conteudo
                            Column(controls=[
                             Text("de R$ 45,90 por:",
                                  size=16),
                             Text("R$ 27,90",
                                  size=23,
                                  color=colors.GREEN_100)
                            ], alignment=MainAxisAlignment.CENTER
                            )
                        ]
                        ),

                        Container(content=ElevatedButton(text='Pedir Agora',
                                                         color=colors.WHITE,
                                                         bgcolor=colors.RED_300),
                                  )

                    ],  # final co controls da minha coluna

                )   # aqui esta acabando a minha coluna


            )   # aqui esta acabando o meu container

        )

    page.add(gridview)

    page.update()


if __name__ == '__main__':
    app(main)
