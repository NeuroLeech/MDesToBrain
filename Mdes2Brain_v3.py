from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from sklearn.ensemble import RandomForestRegressor
import joblib


ThoughtProbes=['I was absorbed in the contents of my thoughts:',
'My thoughts involved other people:',
'I was thinking about solutions to problems (or goals):',
'My thoughts involved words:',
'My thoughts involved sounds:',
'My thoughts involved images:',
'My thoughts involved past events:',
'My thoughts were distracting me from what I was doing:',
'My thoughts were focused on an external task or activity:',
'My thoughts were intrusive:',
'My thoughts were deliberate:',
'My thoughts were detailed and specific:',
'My thoughts involved future events:',
'The emotion of my thoughts was:',
'My thoughts involved myself:',
'My thoughts contained information I already knew (e.g., knowledge or memories):']




app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

heading = html.H4(
    "Generative model linking experience sampling and neural activity", className="bg-primary text-white p-2"
)


Q1 = html.Div(
    [
        dbc.Label(ThoughtProbes[0], html_for="Q1"),
        dcc.Slider(1, 10, value=5, id="Q1",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q2 = html.Div(
    [
        dbc.Label(ThoughtProbes[1], html_for="Q2"),
        dcc.Slider(1, 10, value=5, id="Q2",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q3 = html.Div(
    [
        dbc.Label(ThoughtProbes[2], html_for="Q3"),
        dcc.Slider(1, 10, value=5, id="Q3",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q4 = html.Div(
    [
        dbc.Label(ThoughtProbes[3], html_for="Q4"),
        dcc.Slider(1, 10, value=5, id="Q4",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q5 = html.Div(
    [
        dbc.Label(ThoughtProbes[4], html_for="Q5"),
        dcc.Slider(1, 10, value=5, id="Q5",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q6 = html.Div(
    [
        dbc.Label(ThoughtProbes[5], html_for="Q6"),
        dcc.Slider(1, 10, value=5, id="Q6",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q7 = html.Div(
    [
        dbc.Label(ThoughtProbes[6], html_for="Q7"),
        dcc.Slider(1, 10, value=5, id="Q7",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q8 = html.Div(
    [
        dbc.Label(ThoughtProbes[7], html_for="Q8"),
        dcc.Slider(1, 10, value=5, id="Q8",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q9 = html.Div(
    [
        dbc.Label(ThoughtProbes[8], html_for="Q9"),
        dcc.Slider(1, 10, value=5, id="Q9",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q10 = html.Div(
    [
        dbc.Label(ThoughtProbes[9], html_for="Q10"),
        dcc.Slider(1, 10, value=5, id="Q10",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q11 = html.Div(
    [
        dbc.Label(ThoughtProbes[10], html_for="Q11"),
        dcc.Slider(1, 10, value=5, id="Q11",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q12 = html.Div(
    [
        dbc.Label(ThoughtProbes[11], html_for="Q12"),
        dcc.Slider(1, 10, value=5, id="Q12",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q13 = html.Div(
    [
        dbc.Label(ThoughtProbes[12], html_for="Q13"),
        dcc.Slider(1, 10, value=5, id="Q13",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q14 = html.Div(
    [
        dbc.Label(ThoughtProbes[13], html_for="Q14"),
        dcc.Slider(1, 10, value=5, id="Q14",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q15 = html.Div(
    [
        dbc.Label(ThoughtProbes[14], html_for="Q15"),
        dcc.Slider(1, 10, value=5, id="Q15",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

Q16 = html.Div(
    [
        dbc.Label(ThoughtProbes[15], html_for="Q16"),
        dcc.Slider(1, 10, value=5, id="Q16",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

#app.layout = html.Div(
#    [
#        dcc.Graph(id="graph"),
#    ]
#)


control_panel1 = dbc.Card(
    dbc.CardBody(
        [Q1, Q2,Q3,Q4,Q5,Q6,Q7,Q8],
        className="bg-light",
    )
)

control_panel2 = dbc.Card(
    dbc.CardBody(
        [Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16],
        className="bg-light",
    )
)

daq.BooleanSwitch(id="dark_mode", on=False),

#graph = dbc.Card(
#    [html.Div(id="error_msg", className="text-danger"), dcc.Graph(id="graph")]
#)

graph = dbc.Card(
    #[html.Div(id="error_msg", className="text-danger"), dcc.Graph(id="graph")]
    [html.Div(id="error_msg", className="text-danger"), dcc.Graph(id="graph",style={'width': '100vh', 'height': '100vh'})]
    
)

app.layout = html.Div(
    [heading, dbc.Row([dbc.Col(control_panel1, md=6),dbc.Col(control_panel2, md=6), html.P("See estimated brain", style={"textAlign": "left"}),daq.BooleanSwitch(id="brain", on=False),dbc.Col(graph, md=10)])]
)




@app.callback(
    Output("graph", "figure"),
    #Output("error_msg", "children"),
    Input("Q1", "value"),
    Input("Q2", "value"),
    Input("Q3", "value"),
    Input("Q4", "value"),
    Input("Q5", "value"),
    Input("Q6", "value"),
    Input("Q7", "value"),
    Input("Q8", "value"),
    Input("Q9", "value"),
    Input("Q10", "value"),
    Input("Q11", "value"),
    Input("Q12", "value"),
    Input("Q13", "value"),
    Input("Q14", "value"),
    Input("Q15", "value"),
    Input("Q16", "value"),
    Input("brain", "on"),
)
def callback(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16,brain):

    lvert=np.load('lvert.npy',allow_pickle=True)
    #gradsRaw=np.load('gradsRaw.npy',allow_pickle=True)
    gradsRaw=np.load('gradsNormed.npy',allow_pickle=True)
    n_grad=5
    grads=np.zeros(gradsRaw.shape)
    gradsMean=grads[:,0]
    if brain:
        X=np.asarray([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16]).reshape(1, -1)
        fitted_models=joblib.load("Rep/fitted_models.pkl")


        prediction=np.zeros([n_grad])
        for i, model in enumerate(fitted_models):
            prediction[i] = model.predict(X)[0]

        for i in range(n_grad):
            grads[:,i]=np.asarray(gradsRaw[:,i])*prediction[i]

        gradsMean=grads.mean(axis=1)
        #gradsMean=(gradsMean-gradsMean.mean())/gradsMean.std()

    t = np.linspace(0, 20, 100)
    x, y, z = lvert[:,0],lvert[:,1],lvert[:,2]

    fig = px.scatter_3d(
        x=x,
        y=y,
        z=z,
        color=gradsMean,
    )

    # Set camera viewing angle
    fig.update_layout(
        scene_camera=dict(
            eye=dict(x=-2, y=0, z=0),  # Camera position
            center=dict(x=0, y=0, z=0),     # Point camera looks at
            up=dict(x=0, y=0, z=1)          # Up direction
        ),
        #scene=dict(  # Ensures equal aspect ratio
        #    xaxis_title='X',
        #    yaxis_title='Y',
        #    zaxis_title='Z'
        #)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=False)