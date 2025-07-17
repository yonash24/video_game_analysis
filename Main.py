import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data (e.g., from your Data.avg_critic_by_platform function)
platforms = ['PC', 'PlayStation 5 (PS5)', 'Xbox Series X/S', 'Nintendo Switch', 'Mobile']
avg_scores = [85.5, 90.1, 88.2, 80.5, 65.3]

# Create a Series to simulate the output of avg_critic_by_platform
# The index will be the platforms, and values will be the scores
platform_scores = pd.Series(avg_scores, index=platforms)

plt.figure(figsize=(10, 6))

# Plotting a bar chart
plt.bar(platform_scores.index, platform_scores.values, color='skyblue')

plt.xlabel("Platform")
plt.ylabel("Average Critic Score")
plt.title("Average Critic Score by Platform")

# --- Example of plt.xticks() ---
# Rotate x-axis labels by 45 degrees for better readability
plt.xticks(rotation=45, ha='right') # 'ha' stands for horizontal alignment

plt.grid(axis='y', linestyle='--', alpha=0.7) # Optional: add horizontal grid
plt.tight_layout() # Adjusts plot parameters for a tight layout
plt.show()
