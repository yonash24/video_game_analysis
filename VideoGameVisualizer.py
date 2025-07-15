from DataHandler import Data
import pandas as pd
import matplotlib.pyplot as plt

#class to visualize the data
class visualize:
    
    #Display the number of games released  each year
    #enter here series created from release_in_year in Data class
    def games_by_genre(series:pd.Series):
        plt.figure(figsize=(10,6))
        plt.plot(series.index, series.values, label='games in year', marker='o')
        plt.xlabel("year")
        plt.ylabel("games")
        plt.title("games released by year")
        plt.legend()
        plt.grid(axis='y')
        plt.show()
        
    
    