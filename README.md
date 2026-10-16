# MDES to Brain

Generative model linking multi-dimensional experience sampling (MDES) and neural activity.

Rate 16 thought probes on a 1–10 scale, then toggle **See estimated brain** to see the
predicted cortical pattern. Five random-forest models (`Rep/fitted_models.pkl`) predict
weights for five cortical gradients (`gradsNormed.npy`), which are averaged and drawn on
the cortical surface vertices (`lvert.npy`).

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

`Mdes2Brain_v3.py` is the original Dash version of the app
(needs `dash dash-bootstrap-components dash-daq` installed).
