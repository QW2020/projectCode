#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
gzbd graph
'''

import plotly.graph_objs as go;
import plotly,mysql_utils;

def build_graph_data():
    result = mysql_utils.execute_all("select * from gzbd_epidemic order by date desc limit 7");
    x_date = [];
    y_diagnosis = [];
    y_cure = [];
    y_death = [];
    v_diagnosis = 0;
    v_cure = 0;
    v_death = 0;
    for item in result:
        x_date.append(item[2]);
        y_diagnosis.append(item[3]);
        y_cure.append(item[5]);
        y_death.append(item[6]);
        if item[3] !=None:
            v_diagnosis += item[3];
        if item[5] !=None:
            v_cure += item[5];
        if item[6] != None:
            v_death += item[6];
    graph_data = {
        "x_date": x_date,
        "y_diagnosis": y_diagnosis,
        "y_cure": y_cure,
        "y_death": y_death,
        "v_diagnosis": v_diagnosis,
        "v_cure": v_cure,
        "v_death": v_death
    };
    return graph_data;

def draw_line_graph(graph_data):
    # 准备图轨数据
    trace_1 = go.Scatter(
        x = graph_data.get("x_date"),
        y = graph_data.get("y_diagnosis"),
        name="确诊数"
    );
    trace_2 = go.Scatter(
        x=graph_data.get("x_date"),
        y=graph_data.get("y_cure"),
        name="治愈数"
    );
    trace_3 = go.Scatter(
        x=graph_data.get("x_date"),
        y=graph_data.get("y_death"),
        name="死亡数"
    );
    line_data = [trace_1, trace_2, trace_3];

    # 设置画图布局
    layout = go.Layout(title="冠状病毒-折线图",xaxis={'title':'时间'},yaxis={'title':'数量'});
    # 融合图轨数据和布局
    figure = go.Figure(data=line_data,layout=layout);
    # 输出
    plotly.offline.plot(figure,filename="/python视频/temp/gzbd_line-graph.html",image="png");

def draw_bar_graph(graph_data):
    # 准备图轨数据
    trace_1 = go.Bar(
        x=graph_data.get("x_date"),
        y=graph_data.get("y_diagnosis"),
        name="确诊数"
    );
    trace_2 = go.Bar(
        x=graph_data.get("x_date"),
        y=graph_data.get("y_cure"),
        name="治愈数"
    );
    trace_3 = go.Bar(
        x=graph_data.get("x_date"),
        y=graph_data.get("y_death"),
        name="死亡数"
    );
    bar_data = [trace_1, trace_2, trace_3];

    # 设置画图布局
    layout = go.Layout(title="冠状病毒-柱状图", xaxis={'title': '时间'}, yaxis={'title': '数值'});
    # 融合图轨数据和布局
    figure = go.Figure(data=bar_data, layout=layout);
    # 输出
    plotly.offline.plot(figure, filename="/python视频/temp/gzbd_bar-graph.html", image="png");

def draw_pie_graph(graph_data):
    # 准备图轨数据
    trace_1 = go.Pie(
        labels = ["确诊数","治愈数","死亡数"],
        values = [graph_data.get("v_diagnosis"),graph_data.get("v_cure"),graph_data.get("v_death")]
    );
    pie_data = [trace_1];

    # 设置画图布局
    layout = go.Layout(title="冠状病毒-饼图");
    # 融合图轨数据和布局
    figure = go.Figure(data=pie_data,layout=layout);
    # 输出
    plotly.offline.plot(figure,filename="/python视频/temp/gzbd_pie-graph.html",image="png");


if __name__ == "__main__":
    graph_data = build_graph_data();
    # draw_line_graph(graph_data);
    # draw_bar_graph(graph_data);
    # draw_pie_graph(graph_data);