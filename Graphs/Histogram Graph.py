import matplotlib.pyplot as graph

marks = [70,43,56,91,76,64,71,83,41,76,56,64,64,49,76,94,98,76,73,76,91]
# Using bins to set range between them. You can also use bins = 3 -> creates 3 divisions.
graph.hist(marks,bins=[45,55,65,70,80,85,95,100], rwidth=0.90, color = 'r')
graph.show()