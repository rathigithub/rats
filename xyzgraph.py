import matplotlib.pyplot as plt 
import pyexcel as p
graph = p.get_excel('/home/cl311/Rathi/xyzgraph.csv')
plt.plot(x,y,z)
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.zlabel("Z AXIS")
plt.title("PLOTTING A GRAPH FROM EXCEL")
plt.show()