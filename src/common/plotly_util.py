# -*- coding: utf-8 -*-
import plotly.graph_objects as go

if __name__ == '__main__':
    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.write_html('first_figure.html', auto_open=True)
