import numpy as np
import matplotlib.pyplot as graph

a = np.arange(0,210,30)
x = np.sin(a)

graph.plot(a,x)
graph.show()