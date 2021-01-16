import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import folium
from folium import plugins
from folium.plugins import HeatMap
import plotly.express as px
import json
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, jaccard_score, f1_score, log_loss, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree, neighbors
from mlxtend.plotting import plot_decision_regions
from sklearn.ensemble import RandomForestRegressor
import time

LR_grid = {
           'penalty':['none','l2'],
           'C':[0.001,.009,0.01,.09,1,5,10,25],
           'max_iter': [100,1000]
           }
logistic = LogisticRegression(C=)
CV_LR = GridSearchCV(estimator=LogisticRegression(random_state=42), param_grid = LR_grid,scoring = 'accuracy',cv=5)