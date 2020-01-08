from cutecharts.charts import Line

chart = Line('plot demo')
chart.set_options(
    labels=['one','two','three','four','five'],
    x_label='xLabel',
    y_label='yLabel')

chart.add_series('series-A',[32,54,2,56,34])
chart.add_series('series-B',[90,32,4,23,32])
chart.render()