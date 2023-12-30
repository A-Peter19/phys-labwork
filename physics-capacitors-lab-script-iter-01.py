import matplotlib.pyplot as plt
import numpy as np


#variables containing empirical data from labwork#

x=[0,20,40,60,80,100,120,140,160,180,200,220]

y=[9,8.84,8.41,7.86,7.23,6.54,5.77,4.86,3.88,2.50,1.21,0.32]



#print statements for debugging of variables#

print(x)
print()

print(y)
print()



#Build graph object with variables#

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(x=x, y=y, marker='0', c='r', edgecolor='b')
ax.set_title('Scatter: $x$ versus $y$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')



#command to generate graph using data from above#

plt.show()




