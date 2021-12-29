import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
print(mean)
print(stdev)
fig = ff.create_distplot([data],['reading_time'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.01], mode = 'lines', name = 'mean'))
fig.show()
def randomSetOfMean (counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def showFig (df) :
    mean = statistics.mean(df)
    fig1 = ff.create_distplot([df],['reading_time'],show_hist = False)
    fig1.add_trace(go.Scatter(x = [mean,mean], y = [0,0.01], mode = 'lines', name = 'mean'))
    fig1.show()
def setup () :
    df = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        df.append(setOfMeans)
    showFig(df)
    mean = statistics.mean(df)
    stdev = statistics.stdev(df)
    print(mean)           
    print(stdev)
    print(len(df))
setup()               