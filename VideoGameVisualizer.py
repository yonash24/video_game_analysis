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

        
    #See how average critic scores have changed over time.
    #insert a series output fron avg_critic_score_per_time in Data
    @staticmethod
    def avg_score_over_time(series:pd.Series):
        plt.figure(figsize=(10.6))
        plt.plot(series.index, series.values, label="yearly critic score")
        plt.xlabel("year")
        plt.ylabel("avg critic score")
        plt.title("average critic score per year")
        plt.legend()
        plt.grid()
        plt.show()
        
        
    #Show the proportion of games belonging to the most popular n genres 
    #get the number of top genres you want and series from count_by_genre from Data
    @staticmethod
    def games_by_genre(n, series:pd.Series):
        new_series = series.head(n)
        plt.figure(figsize=(10,6))
        plt.pie(new_series.values,
                labels=new_series.index,
                autopct='%1.1f%%',
                startangle=90)
        plt.title("top n games by genre")
        plt.show()   
        
        
    
    #Compare how sales in different regions (e.g., NA, EU, JP) have evolved over time on a single graph
    #get dataset from add_year
    @staticmethod
    def regionals_sales_trend(na_series:pd.Series, jp_series:pd.Series, pal_series:pd.Series):
        plt.figure(figsize=(10,6))
        plt.plot(na_series.index, na_series.values,label="na_sales", marker='o')
        plt.plot(jp_series.index, jp_series.values,label="jp_sales", marker='o')
        plt.plot(pal_series.index, pal_series.values,label="pal_sales", marker='o')
        plt.xlabel("year")
        plt.ylabel("region")
        plt.title("region sales")
        plt.legend()
        plt.grid(True)
        plt.show()
        
        
    #Compare the average critic scores of games across different gaming platforms
    #get series from avg_critic_by_platform from data
    @staticmethod
    def avg_critic_score_by_platform(series:pd.Series):
        plt.figure(figsize=(10,6))
        plt.bar(series.index, series.values)
        plt.xlabel("platform")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("avg critic score")
        plt.title("average critic score by platform")
        plt.grid(axis='y')
        plt.show()        
        
        
    #Track and compare the sales performance of a few chosen publishers
    #get series from sales_by_chosen_publishers from Data
    @staticmethod
    def publisher_sales_trend(series:pd.Series):
        plt.figure(figsize=(10,6))
        plt.bar(series.index, series.values, label="sales")
        plt.xlabel("publisher")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("sales")
        plt.title("chosen publisher sailes")
        plt.grid(axis='y')
        plt.show()
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    