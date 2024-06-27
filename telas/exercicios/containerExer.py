from flet import *


def main(page: Page):

    page.title = "Atividade Container - 1"

    container1 = Container(
        content=Column(
            controls=[
                Row(controls=[
                    Image(src='../imagens/inspector.png')
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text('O Inspetor', size=18)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text('Inglaterra, 24 de desembro 1897. '
                         'È época de natal e Leonardo Jones um detetive respeitado é chamado para resolver um ultimo '
                         'caso antes que possa sair de ferias, porem, a investigação não vai como o esperado e agora '
                         'ele terá que lutar contra uma conspiração que está tomando força por toda Londres.',
                         width=290,
                         text_align=TextAlign.JUSTIFY)
                ])
            ], horizontal_alignment="center",
        ),


        border_radius=border_radius.all(10),

        margin=margin.all(10),

        shadow=BoxShadow(
            spread_radius=10,
            blur_radius=10,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER
        ),
    )

    container2 = Container(
        content=Column(
            controls=[
                Row(controls=[
                    Image(src='../imagens/fada_sonhos.png')
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text('A Fada dos Sonhos',
                         size=18)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text('A lenda de uma pequena fada que com seu posinho magico ajuda as crianças a não '
                         'terem pesadelos durante seus sonos.',
                         width=290,
                         text_align=TextAlign.JUSTIFY)
                ])
            ], horizontal_alignment="center",

        ),
        border_radius=border_radius.all(10),

        margin=margin.all(10),

        shadow=BoxShadow(
            spread_radius=10,
            blur_radius=10,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER
        ),
    )

    container3 = Container(
        content=Column(
            controls=[
                Row(controls=[
                    Image(src='../imagens/holandes_voador.png')
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text('Holandes Voador', size=18)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text('Um lendario navio fantasma que gerou muitas landas a respeito de sua lendaria tripulação,'
                         'e seu lendario capitão: Rocks D. Jonnes.',
                         width=290,
                         text_align=TextAlign.JUSTIFY)
                ])
            ], horizontal_alignment="center",
        ),

        border_radius=border_radius.all(10),

        margin=margin.all(10),

        shadow=BoxShadow(
            spread_radius=10,
            blur_radius=10,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER
        ),
    )

    linha = Row(controls=[container1, container2, container3])

    page.add(linha)
    page.update()


if __name__ == '__main__':
    app(main)
