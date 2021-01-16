import dash
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

df = pd.read_csv("Data-Collisions.csv")

print(df.head())