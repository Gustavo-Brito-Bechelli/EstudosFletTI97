from flet import *
import math


def main(page: Page):

    page.title = 'Trabalhando cim Containers'

    # container precisa de altura e largura
    container1 = Container(
        content=Text('Texto 1',
                     size=30,
                     width=FontWeight.W_500,
                     color='#000000'),
        bgcolor=colors.BLUE,

        width=200,

        height=200,
        # padding=20,
        # padding=padding.symmetric(vertical=80, horizontal=50),

        # padding=padding.only(top=155, left=53),     # afasta o conteudo interno em relação a borda
        # border=border.all(5, color=colors.RED)

        border=border.only(top=BorderSide(5, color=colors.YELLOW)),

        margin=margin.all(10),   # afasta o conteudo externo em relação a borda
        # margin=margin.only(top=200, left=100),
        # margin=margin.symmetric(vertical=100),

        # gradient=LinearGradient(      # trabalha cor camaleão
        #     begin=alignment.bottom_center,
        #     end=alignment.bottom_center,
        #     colors=[colors.BLACK, colors.WHITE]
        # ),
        # gradient=RadialGradient(
        #     colors=[colors.RED, colors.ORANGE]
        # ),
        # gradient=SweepGradient(
        #     center=alignment.center,
        #     start_angle=0.0,
        #     end_angle=math.pi * 2,
        #     colors=[colors.CYAN, colors.PINK]
        # ),

        # border_radius=border_radius.all(30)      # arredonda as bordas
        border_radius=border_radius.only(top_left=10, top_right=10),

        image_src='../imagens/Login.png',

        shadow=BoxShadow(
            spread_radius=10,   # borda branca antes da sombra
            blur_radius=10,     # desfoque
            color=colors.BLUE_GREY_300,     # cor
            offset=Offset(0, 0),      # trabalha eixos X e Y
            blur_style=ShadowBlurStyle.OUTER    # o tipo de shadow
        ),

        alignment=Alignment(0, 0)       # (x, y), o centro é 0
    )

    container2 = Container(
        content=Column(controls=[
            Text('1', bgcolor=colors.YELLOW),
            Text('2', bgcolor=colors.YELLOW),
            Text('3', bgcolor=colors.YELLOW)
        ]),

        width=200,

        height=200,
        # padding=20,
        # padding=padding.symmetric(vertical=80, horizontal=50),

        # padding=padding.only(top=155, left=53),     # afasta o conteudo interno em relação a borda
        # border=border.all(5, color=colors.RED)

        border=border.only(top=BorderSide(5, color=colors.YELLOW)),

        margin=margin.all(10),   # afasta o conteudo externo em relação a borda
        # margin=margin.only(top=200, left=100),
        # margin=margin.symmetric(vertical=100),

        # gradient=LinearGradient(      # trabalha cor camaleão
        #     begin=alignment.bottom_center,
        #     end=alignment.bottom_center,
        #     colors=[colors.BLACK, colors.WHITE]
        # ),
        # gradient=RadialGradient(
        #     colors=[colors.RED, colors.ORANGE]
        # ),
        # gradient=SweepGradient(
        #     center=alignment.center,
        #     start_angle=0.0,
        #     end_angle=math.pi * 2,
        #     colors=[colors.CYAN, colors.PINK]
        # ),

        # border_radius=border_radius.all(30)      # arredonda as bordas
        border_radius=border_radius.only(top_left=10, top_right=10),

        shadow=BoxShadow(
            spread_radius=10,   # borda branca antes da sombra
            blur_radius=10,     # desfoque
            color=colors.BLUE_GREY_300,     # cor
            offset=Offset(0, 0),      # trabalha eixos X e Y
            blur_style=ShadowBlurStyle.OUTER    # o tipo de shadow
        ),

        alignment=Alignment(0, 0)       # (x, y), o centro é 0
    )

    linha = Row(controls=[container1, container1, container2])
    page.add(linha)
    page.update()


if __name__ == '__main__':
    app(main)
