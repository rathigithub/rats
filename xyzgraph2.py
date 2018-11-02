import matplotlib.pyplot as plt 
import pandas as pd
import csv
x=[]
y=[]
graph = pd.read_csv('/home/cl311/Rathi/xyz.csv')
plt.plot(x,y)
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.title("PLOTTING A GRAPH FROM EXCEL")
plt.show()