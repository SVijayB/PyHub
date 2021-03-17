import numpy as np
import matplotlib.pyplot as graph

a = np.arange(0, 210, 30)
x = np.cos(a)

graph.title("COS GRAPH")
graph.xlabel("Degrees")
graph.ylabel("Values")
graph.plot(a, x)
graph.show()
