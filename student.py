#data_analysis.py
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("student.csv")
student_df = df.loc[df['student_id']=='TRL_xsl']

print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(orientation = 'h', x = student_df.groupby("level")["attempt"].mean(), y = ['Level 1', 'Level 2', 'Level 3', 'Level 4']))

fig.show()