# plottask.py
# This Program is to generate the norman distribution of 1000 values
# Create Histogram of this values
# need to plot the function of x^3
# plot the graph and given titel axis name and legend to the graph
# save the graph in file
# Aurthir: Akshay Pastagiya

# import library of numpy and matlib
import numpy as np
import matplotlib.pyplot as plt

# create 1000 normal distribution values
# set mean and standard devitation
mean = 5
devitation = 2
values = np.random.normal(mean,devitation,1000)

# generate values for h(x) = x^3 in the range between 0 to 10
x = np.linspace(0,10,1000)
y = x*x*x

# plot histogram
plt.hist(values, label = "Normal Distrubutation Histogram")
# plot function graph
plt.plot(x,y,label = "x cube", color = 'r')
plt.title("Histogram and function plot")
plt.legend()

# Save Plot
plt.savefig("plottask.png")