#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
画图
'''

import plotly.graph_objs as go;
import plotly;

def draw_line_graph():
    # 准备图轨数据
    trace_1 = go.Scatter(
        x = [1,2,3,4],
        y = [8,9,12,13],
        name="散点图",
        mode='markers'
    );
    trace_2 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[15,5,8,16],
        name="折线图"
    );
    line_data = [trace_1, trace_2];

    # 设置画图布局
    layout = go.Layout(title="折线图",xaxis={'title':'x'},yaxis={'title':'y'});
    # 融合图轨数据和布局
    figure = go.Figure(data=line_data,layout=layout);
    # 输出
    plotly.offline.plot(figure,filename="/python视频/temp/line-graph.html",image="png");

def draw_bar_graph():
    # 准备图轨数据
    trace_1 = go.Bar(
        x=[1, 2, 3, 4],
        y=[25, 28, 30, 32],
        name="第一产业"
    );
    trace_2 = go.Bar(
        x=[1, 2, 3, 4],
        y=[20, 12, 25, 24],
        name="第二产业"
    );
    trace_3 = go.Bar(
        x=[1, 2, 3, 4],
        y=[22, 25, 23, 10],
        name="第三产业"
    );
    bar_data = [trace_1, trace_2, trace_3];

    # 设置画图布局
    layout = go.Layout(title="柱状图", xaxis={'title': '季度'}, yaxis={'title': '产值'});
    # 融合图轨数据和布局
    figure = go.Figure(data=bar_data, layout=layout);
    # 输出
    plotly.offline.plot(figure, filename="/python视频/temp/bar-graph.html", image="png");

def draw_line_graph():
    # 准备图轨数据
    trace_1 = go.Pie(
        labels = ["产品一","产品二","产品三","产品四","产品五"],
        values = [12.3,15.2,16.5,11.3,27.8]
    );
    pie_data = [trace_1];

    # 设置画图布局
    layout = go.Layout(title="饼图");
    # 融合图轨数据和布局
    figure = go.Figure(data=pie_data,layout=layout);
    # 输出
    plotly.offline.plot(figure,filename="/python视频/temp/pie-graph.html",image="png");


if __name__ == "__main__":
    # draw_line_graph();
    # draw_bar_graph();
    draw_line_graph();