import matplotlib.pyplot as plt
import pandas as pd

# 1. Create a sample DataFrame (or use your loaded video game data)
data = {'Year': [2000, 2005, 2010, 2015, 2020],
        'Global_Sales_Millions': [50, 75, 90, 80, 110],
        'NA_Sales_Millions': [20, 30, 35, 30, 45]}
df = pd.DataFrame(data)

# 2. Use Matplotlib's plot function directly with DataFrame columns
plt.figure(figsize=(10, 6)) # Optional: set figure size
plt.plot(df['Year'], df['Global_Sales_Millions'], label='Global Sales', marker='o',color='lightgreen')
plt.plot(df['Year'], df['NA_Sales_Millions'], label='NA Sales', marker='x', linestyle='--')

# 3. Add labels, title, and legend for clarity
plt.xlabel('Release Year')
plt.ylabel('Sales (Millions)')
plt.title('Video Game Sales Trends')
plt.legend() # Displays the labels for each line
plt.grid(True) # Adds a grid for easier reading

# 4. Display the plot
plt.show()