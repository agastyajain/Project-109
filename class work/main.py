import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

df = pd.read_csv("height-weight.csv")
#weight = df["Height(Inches)"].tolist()
weight = df["Weight(Pounds)"].tolist()

mean = sum(weight)/len(weight)
median = statistics.median(weight)
mode = statistics.mode(weight)
st_dev = statistics.stdev(weight)

firstStDevStart = mean - st_dev
firstStDevEnd = mean + st_dev

secondStDevStart = mean - 2*st_dev
secondStDevEnd = mean + 2*st_dev

thirdStDevStart = mean - 3*st_dev
thirdStDevEnd = mean + 3*st_dev

dataBetweenFirstStDev = 0
dataBetweenSecondStDev = 0
dataBetweenThirdStDev = 0

for num in weight:
    if num > firstStDevStart and num < firstStDevEnd:
        dataBetweenFirstStDev = dataBetweenFirstStDev + 1
    if num > secondStDevStart and num < secondStDevEnd:
        dataBetweenSecondStDev = dataBetweenSecondStDev + 1
    if num > thirdStDevStart and num < thirdStDevEnd:
        dataBetweenThirdStDev = dataBetweenThirdStDev + 1

dataBetweenFirstStDev = (dataBetweenFirstStDev/len(weight)) * 100
dataBetweenSecondStDev = (dataBetweenSecondStDev/len(weight)) * 100
dataBetweenThirdStDev = (dataBetweenThirdStDev/len(weight)) * 100

print("The mean of the data is " + str(mean))
print("The median of the data is " + str(median))
print("The mode of the data is " + str(mode))
print("The Standard Deviation of the data is " + str(st_dev))
print("The data within first Standard Deviation is {}%".format(dataBetweenFirstStDev))
print("The data within second Standard Deviation is {}%".format(dataBetweenSecondStDev))
print("The data within third Standard Deviation is {}%".format(dataBetweenThirdStDev))

fig = ff.create_distplot([weight],["Weight(Pounds)"],show_hist=False)
#fig = ff.create_distplot([weight],["Height(Inches)"],show_hist=False)
fig.show()