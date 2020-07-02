import numpy as np
import matplotlib.pyplot as graph

a = np.arange(0,80,10)
x = np.tan(a)

graph.title("TAN GRAPH")
graph.xlabel("Degrees")
graph.ylabel("Values")
graph.plot(a,x)
graph.show()