import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

dice_data=[]

for i in range(1,100000):
    num1= random.randint(1,6)
    num2= random.randint(1,6)
    dice_data.append(num1+num2)

mean = sum(dice_data)/len(dice_data)
median = statistics.median(dice_data)
mode = statistics.mode(dice_data)
st_dev = statistics.stdev(dice_data)

firstStDevStart = mean - st_dev
firstStDevEnd = mean + st_dev

secondStDevStart = mean - 2*st_dev
secondStDevEnd = mean + 2*st_dev

thirdStDevStart = mean - 3*st_dev
thirdStDevEnd = mean + 3*st_dev

dataBetweenFirstStDev = 0
dataBetweenSecondStDev = 0
dataBetweenThirdStDev = 0

for num in dice_data:
    if num > firstStDevStart and num < firstStDevEnd:
        dataBetweenFirstStDev = dataBetweenFirstStDev + 1
    if num > secondStDevStart and num < secondStDevEnd:
        dataBetweenSecondStDev = dataBetweenSecondStDev + 1
    if num > thirdStDevStart and num < thirdStDevEnd:
        dataBetweenThirdStDev = dataBetweenThirdStDev + 1

dataBetweenFirstStDev = (dataBetweenFirstStDev/len(dice_data)) * 100
dataBetweenSecondStDev = (dataBetweenSecondStDev/len(dice_data)) * 100
dataBetweenThirdStDev = (dataBetweenThirdStDev/len(dice_data)) * 100

print("The mean of the data is " + str(mean))
print("The median of the data is " + str(median))
print("The mode of the data is " + str(mode))
print("The Standard Deviation of the data is " + str(st_dev))
print("The data within first Standard Deviation is {}%".format(dataBetweenFirstStDev))
print("The data within second Standard Deviation is {}%".format(dataBetweenSecondStDev))
print("The data within third Standard Deviation is {}%".format(dataBetweenThirdStDev))

fig = ff.create_distplot([dice_data],["Dice Data"],show_hist=False)
fig.show()