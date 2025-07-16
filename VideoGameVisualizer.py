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
        
    
    #Display distribution games by platform
    #get a series from game_in_platform in Data class
    @staticmethod
    def games_by_platform(series:pd.Series):
        plt.figure(figsize=(10,6))
        plt.bar(series.index,series.values,label='game by platform')
        plt.xlabel('consule')
        plt.ylabel("number of games")
        plt.title("number of games per console")
        plt.legend()
        plt.grid(axis='y')
        plt.show()
        
    #Highlight the publishers with the highest total sales
    #get a dataset fron get_top_publisher_salse
    @staticmethod
    def top_publisher_sales(dataset:pd.Series):
        plt.figure(figsize=(10,6))
        plt.bar(dataset.index, dataset.values, label="highest sales")
        plt.xlabel("publishers")
        plt.ylabel("slaes")
        plt.title("top publishers with highest sales")
        plt.legend()
        plt.grid(axis='y')
        plt.show
    
    #Explore the relationship (correlation) between a game's sales and its critic score
    @staticmethod
    def sales_vs_scores(dataset:pd.DataFrame):
        plt.figure(figsize=(12,8))
        plt.scatter(dataset["total_sales"], dataset["critic_score"], label="score per sale")
        plt.xlabel("sales")
        plt.ylabel("critic score")
        plt.title("score per sale")
        plt.legend()
        plt.grid(True)
        plt.show()

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    