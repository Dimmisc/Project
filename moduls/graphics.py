import plotly.graph_objects as go
from .Site_moduls import GetDataStudents


def StudentsPlot(db_sess):
    datag = GetDataStudents(db_sess)
    const_max = max(datag[0])
    lengr = len(datag[0])
    arg = 13
    fig = go.Figure()
    for step in range(lengr - arg):
        if step == 0:
            fig.add_trace(go.Bar(visible=False,y=datag[1] ))
        else:
            fig.add_trace(go.Bar(visible=False,x=datag[0][step-1:step+arg-1] + ["vosid"],y=datag[1][step-1:step+arg-1] + [const_max]))
    fig.data[0].visible = True
    go.Bar()
    steps = []
    for i in range(len(fig.data)):
        step = dict(method="update",args=[{"visible": [False] * len(fig.data)}],)
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)
    sliders = [dict(active=0,pad={"t": 11},steps=steps)]
    fig.update_layout(sliders=sliders)
    return fig.to_html(full_html=False, config={'displayModeBar': False})

