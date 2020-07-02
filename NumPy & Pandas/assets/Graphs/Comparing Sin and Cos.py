import numpy as np
import matplotlib.pyplot as graph

a = np.arange(0,210,30)
x = np.cos(a)
y = np.sin(a)

graph.title("SIN AND COS GRAPH")
graph.xlabel("Degrees")
graph.ylabel("Values")
graph.plot(a,x,color = 'r', label = "Cos")
graph.plot(a,y,color = 'g',label = "Sin")
graph.legend()
graph.show()