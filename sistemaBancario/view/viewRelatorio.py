from flet import (UserControl, ElevatedButton, Container, icons, colors, LineChartData, Row,
                  LineChartDataPoint, LineChart, Border, BorderSide, ChartAxis, ChartAxisLabel,
                  Text, FontWeight, margin, DatePicker, TextField, Dropdown, dropdown, ResponsiveRow,
                  Column, MainAxisAlignment, IconButton, ButtonStyle, MaterialState, RoundedRectangleBorder,
                  CrossAxisAlignment)

from datetime import datetime
from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewRelatorio(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.calendario = DatePicker(
            first_date=datetime(year=2010, month=1, day=1),
            last_date=datetime(year=2045, month=1, day=1)
        )
        self.t_field_calendario = TextField(label='Data')
        self.btn_calendario = IconButton(icon=icons.CALENDAR_MONTH_OUTLINED,
                                         icon_color=self.cores.corDefault,
                                         icon_size=35)
        self.grafico = LineChart(
            data_series=self.dados1(),
            border=Border(
                bottom=BorderSide(4, colors.with_opacity(0.5, colors.ON_SURFACE))
            ),
            left_axis=self.labelAxisLeft(),
            bottom_axis=self.labelAxisBottom(),
            tooltip_bgcolor=colors.with_opacity(0.8, colors.BLUE_GREY),
            min_y=0,
            max_y=4,
            min_x=0,
            max_x=14,
            # animate=5000,
            expand=True,
            )
        self.btn_pesquisar = ElevatedButton(text='Pesquisar', icon=icons.SEARCH_OUTLINED,
                                            expand=True,
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                },
                                                shape=RoundedRectangleBorder(radius=5),
                                            )
                                            )
        self.barra = Container()
        self.dropCategoria = Dropdown(
            label='Categorias',
            options=self.carregarCategorias()
        )

    def build(self):
        linhaBtnPesquisar = Row(col=12,
                                controls=[self.btn_pesquisar],
                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER)

        barraOpcoes = ResponsiveRow(controls=[
            Column(col={'md': 3, }, controls=[self.t_field_calendario]),
            Column(col=1, controls=[self.btn_calendario]),
            Column(col={'md': 4, }, controls=[self.dropCategoria]),
            Column(col={'md': 2, }, controls=[linhaBtnPesquisar])
        ], alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER)

        grafico = ResponsiveRow(controls=[Container(content=self.grafico)])

        return Column(controls=[barraOpcoes, grafico])

    def dados1(self) -> list:
        """
        organiza os daos do banco de dados para construção do grafico
        :return: list de LineChatData
        """
        data_1 = [
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 1),
                    LineChartDataPoint(3, 1.5),
                    LineChartDataPoint(5, 1.4),
                    LineChartDataPoint(7, 3.4),
                    LineChartDataPoint(10, 2),
                    LineChartDataPoint(12, 2.2),
                    LineChartDataPoint(13, 1.8),
                ],
                stroke_width=8,
                color=colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 1),
                    LineChartDataPoint(3, 2.8),
                    LineChartDataPoint(7, 1.2),
                    LineChartDataPoint(10, 2.8),
                    LineChartDataPoint(12, 2.6),
                    LineChartDataPoint(13, 3.9),
                ],
                color=colors.PINK,
                below_line_bgcolor=colors.with_opacity(0, colors.PINK),
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 2.8),
                    LineChartDataPoint(3, 1.9),
                    LineChartDataPoint(6, 3),
                    LineChartDataPoint(10, 1.3),
                    LineChartDataPoint(13, 2.5),
                ],
                color=colors.CYAN,
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
        ]

        return data_1

    def labelAxisLeft(self):
        """
        função para fazer o eixo da esquerda
        :return:
        """
        eixoEsqurda= ChartAxis(
            labels=[
                ChartAxisLabel(
                    value=1,
                    label=Text("1m", size=14, weight=FontWeight.BOLD),
                ),
                ChartAxisLabel(
                    value=2,
                    label=Text("2m", size=14, weight=FontWeight.BOLD),
                ),
                ChartAxisLabel(
                    value=3,
                    label=Text("3m", size=14, weight=FontWeight.BOLD),
                ),
                ChartAxisLabel(
                    value=4,
                    label=Text("4m", size=14, weight=FontWeight.BOLD),
                ),
                ChartAxisLabel(
                    value=5,
                    label=Text("5m", size=14, weight=FontWeight.BOLD),
                ),
                ChartAxisLabel(
                    value=6,
                    label=Text("6m", size=14, weight=FontWeight.BOLD),
                ),
            ],
            labels_size=40,
        )

        return eixoEsqurda

    def labelAxisBottom(self):
        """

        :return:
        """
        eixoInterior = ChartAxis(
            labels=[
                ChartAxisLabel(
                    value=1,
                    label=Container(
                        Text(
                            "SEP",
                            size=16,
                            weight=FontWeight.BOLD,
                            color=colors.with_opacity(0.5, colors.ON_SURFACE),
                        ),
                        margin=margin.only(top=10),
                    ),
                ),
                ChartAxisLabel(
                    value=3,
                    label=Container(
                        Text(
                            "OCT",
                            size=16,
                            weight=FontWeight.BOLD,
                            color=colors.with_opacity(0.5, colors.ON_SURFACE),
                        ),
                        margin=margin.only(top=10),
                    ),
                ),
                ChartAxisLabel(
                    value=5,
                    label=Container(
                        Text(
                            "DEC",
                            size=16,
                            weight=FontWeight.BOLD,
                            color=colors.with_opacity(0.5, colors.ON_SURFACE),
                        ),
                        margin=margin.only(top=10),
                    ),
                ),

                ChartAxisLabel(
                    value=9,
                    label=Container(
                        Text(
                            "JAN",
                            size=16,
                            weight=FontWeight.BOLD,
                            color=colors.with_opacity(0.5, colors.ON_SURFACE),
                        ),
                        margin=margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        )

        return eixoInterior

    def carregarCategorias(self) -> list:
        """

        :return:
        """
        categorias=[
                dropdown.Option('Alimentação'),
                dropdown.Option('Locomoção'),
                dropdown.Option('Lazer'),
                dropdown.Option('Luz'),
                dropdown.Option('Internet'),
            ]

        return categorias
