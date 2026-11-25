import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
plt.plot() # You pass X and Y inside here
plt.scatter() # You pass X and Y inside here as well
plt.bar() # You pass X and the height here
plt.barh() # You pass X and the width here
'''

#Data
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,scalex=True, scaley=True)

#Add labels and title
plt.title("Simple Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

#Display the grid
plt.grid(True)

#Saving the plot
# IMPORTANT: Do this BEFORE showing the graph as it wont save
plt.savefig('Line_Graph.png')

#Show the plot
plt.show()