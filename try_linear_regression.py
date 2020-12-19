from LinearRegression import LinearRegression
import numpy as np


x= []
y = []
with open("ex1data1.txt", mode='r') as file:
    for idx, lines in enumerate(file):
        #print(idx, lines)
        line = lines.split(",")
        #print(line)
        x.append(float(line[0]))
        y.append(float(line[1]))


x = np.asarray(x)
y = np.asarray(y)
x = x.reshape(x.shape[0], 1)
y = y.reshape(y.shape[0], 1)
print(x.shape)
print(y.shape)


model = LinearRegression()
model.fit(x, y)
model.plotdata(x, y)
model.plotregressor(x, y)
model.plotcost(x, y)
