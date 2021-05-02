import pandas as pd
import plotly.express as px
import csv

dataPath = input("Please enter the csv data file path: ")

df = pd.read_csv(dataPath)

with open(dataPath, newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

dataValues = str(file_data[0])

values = dataValues.split(',')

value0 = str(values[0])
value1 = str(values[1])

value0 = value0.replace('[', '')
value1 = value1.replace(']', '')
#for i in enumerate(df):
#    if i == 0:
#        i.split(',')
#        xVal = i[0]
#
#for j in enumerate(df):
#    if j == 0:
#        j.split(',')
#        yVal = i[1]

def graphData():
    fig = px.scatter(df, x = value0, y = value1)
    fig.show()

if(dataPath != ''):
    print("Graph generating...")
    graphData()