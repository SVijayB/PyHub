import numpy as np
import matplotlib.pyplot as graph

a = np.arange(0, 10, 1)
x = np.sqrt(a)

graph.title("SQUARE ROOT GRAPH")
graph.xlabel("Numbers")
graph.ylabel("Values")
graph.plot(a, x, color="r")
graph.show()
