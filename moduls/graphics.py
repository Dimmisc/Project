import plotly.graph_objects as go
from .Site_moduls import GetDataStudents, GetGradesData, GetGradeStudentsData


def StudentsPlot(db_sess):
    data_students = GetDataStudents(db_sess)
    if data_students == False:
        return "<h1>There isn't any data to do graphic</h1>"
    const_max = max(data_students[0])
    lengr = len(data_students[0])
    arg = 30
    fig = go.Figure()
    for step in range(lengr - arg):
        if step == 0:
            fig.add_trace(go.Bar(visible = False, y = data_students[1] ))
        else : 
            fig.add_trace(go.Bar(visible = False, x = data_students[0][step - 1:step + arg - 1] + ["-_-"], y=data_students[1][step - 1:step + arg - 1] + [15]))
    fig.data[0].visible = True
    go.Bar()
    steps = []
    for i in range(len(fig.data)):
        step = dict(method="update",args=[{"visible": [False] * len(fig.data)}],)
        step["args"][0]["visible"][i] = True  # Toggle this trace to "visible"
        steps.append(step)
    sliders = [dict(active=0,pad={"t": 11},steps=steps)]
    fig.update_layout(sliders=sliders)
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def GradesPlot(db_sess):
    data = GetGradesData(db_sess)
    if data == False:
        return "<h1>There isn't any data to do graphic</h1>"
    print(data)
    const_max = data[2]
    lengr = len(data[0])
    arg = 30
    fig = go.Figure()
    for step in range(lengr - arg):
        if step == 0:
            fig.add_trace(go.Bar(visible=False, y=data[1] ))
        else:
            fig.add_trace(go.Bar(visible=False, x=data[0][step - 1:step + arg - 1] + ["-_-"], y=data[1][step - 1:step + arg - 1] + [15]))
    if arg > lengr:
        fig.add_trace(go.Bar(visible=True, x=data[0], y=data[1] ))
        return fig.to_html(full_html=False, config={'displayModeBar': False})
    fig.data[0].visible = True
    steps = []
    for i in range(len(fig.data)):
        step = dict(method="update",args=[{"visible": [False] * len(fig.data)}],)
        step["args"][0]["visible"][i] = True  # Toggle this trace to "visible"
        steps.append(step)
    sliders = [dict(active=0, pad={"t": 11}, steps=steps)]
    fig.update_layout(sliders=sliders)
    return fig.to_html(full_html=False, config={'displayModeBar': False})


def GradeStudentsPlot(db_sess, id_grade):
    data = GetGradeStudentsData(db_sess, id_grade)
    if data == False:
        return "<h1>There isn't any data to do graphic</h1>"
    print(data)
    const_max = data[2]
    fig = go.Figure()
    fig.add_trace(go.Bar(visible=True, x=data[0] + ["Max"], y=data[1] + [15 ]))
    return fig.to_html(full_html=False, config={'displayModeBar': False})