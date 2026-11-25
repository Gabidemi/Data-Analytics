import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sales = pd.DataFrame({
    "Month": [1,2,3,4,5,6],
    "qty_sold": [45,34,62,55,69,72]
})

# plot line graph with markers
plt.plot(
    sales["Month"],
    sales["qty_sold"],
    marker = 'o' # Adds dots on each data poimt
)

# Title and labels
plt.title("Sales at 6 months")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")

#Show the grid
plt.grid(True)

# Save the graph
plt.savefig("Line_Graph_2.png")

# Show the graph
plt.show()