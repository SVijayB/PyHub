import numpy as np
import matplotlib.pyplot as graph

a = np.arange(0, 210, 30)
x = np.sin(a)

graph.title("SIN GRAPH")
graph.xlabel("Degrees")
graph.ylabel("Values")
graph.plot(a, x)
graph.show()
