import warnings

import joblib
import numpy as np
import plotly.express as px
import streamlit as st
from sklearn.exceptions import InconsistentVersionWarning

# The models were pickled with scikit-learn 1.4.1; predictions are identical
# under newer versions, so silence the version-mismatch warning.
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


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

n_grad=5


@st.cache_resource
def load_data():
    lvert=np.load('lvert.npy',allow_pickle=True)
    gradsRaw=np.load('gradsNormed.npy',allow_pickle=True)
    fitted_models=joblib.load("Rep/fitted_models.pkl")
    return lvert, gradsRaw, fitted_models


st.set_page_config(page_title="MDES to Brain", layout="wide")
st.title("Generative model linking experience sampling and neural activity")

lvert, gradsRaw, fitted_models = load_data()

answers=[]
col1, col2 = st.columns(2)
for i, probe in enumerate(ThoughtProbes):
    with (col1 if i < 8 else col2):
        answers.append(st.slider(probe, 1, 10, 5, key=f"Q{i+1}"))

brain = st.toggle("See estimated brain", value=False)

grads=np.zeros(gradsRaw.shape)
gradsMean=grads[:,0]
if brain:
    X=np.asarray(answers).reshape(1, -1)

    prediction=np.zeros([n_grad])
    for i, model in enumerate(fitted_models):
        prediction[i] = model.predict(X)[0]

    for i in range(n_grad):
        grads[:,i]=np.asarray(gradsRaw[:,i])*prediction[i]

    gradsMean=grads.mean(axis=1)

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
    height=800,
)

st.plotly_chart(fig, theme=None, width="stretch")
