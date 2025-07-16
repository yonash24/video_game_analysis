import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

class Data:
    
    #download the data set and return it as a data fram
    @staticmethod
    def get_video_game_data():
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files("asaniczka/video-game-sales-2024", path = '.', unzip= True)
        
        directory_files = os.listdir(".")
        csv_files = []
        for file in directory_files:
            suffix = os.path.splitext(file)[1]
            if suffix == ".csv":
                csv_files.append(file)
        
        cur_size = 0
        data_file = None
        
        if csv_files:
            for file in csv_files:
                if os.path.getsize(file) > cur_size:
                    cur_size = os.path.getsize(file)
                    data_file = file
        
        if data_file:
            try:
                os.rename(data_file,"videoGame_dataset.csv")
            except FileNotFoundError:
                print(f"the dataset file not found")
            except Exception as e:
                print(f"an error occured {e}")
                
            data_set_frame = pd.read_csv("videoGame_dataset.csv")
            return data_set_frame
        
        
    #clean the data 
    #remove all the rows that dont have sales
    @staticmethod
    def remove_unsolds_products(dataset:pd.DataFrame):
        clean_data = dataset[(dataset['total_sales'] != 0) & (dataset['total_sales'].notna())]
        return clean_data
            
    
    #get a dataframe and make a csv file out of him
    @staticmethod
    def data_to_csv(dataset:pd.DataFrame):
        try:
            dataset.to_csv("videoGame_dataset.csv", index= False)
        except Exception as e:
            print(f"exception {e} has occured")
        
    #sort the dataset by paarameter
    @staticmethod
    def sort_data(param,dataset:pd.DataFrame):
        if param == "console":
            dataset = dataset.sort_values(by="console", ascending=False)
        elif param == "title":
            dataset = dataset.sort_values(by="title", ascending=False)
        elif param == "genre":
            dataset = dataset.sort_values(by="genre", ascending=False)
        elif param == "publisher":
            dataset = dataset.sort_values(by="publisher", ascending=False)    
        elif param == "developer":
            dataset = dataset.sort_values(by="developer", ascending=False)
        elif param == "critic_score":
            dataset = dataset.sort_values(by="critic_score", ascending=False)    
        elif param == "total_sales":
            dataset = dataset.sort_values(by="total_sales", ascending=False)
        elif param == "na_sales":
            dataset = dataset.sort_values(by="na_sales", ascending=False) 
        elif param == "jp_sales":
            dataset = dataset.sort_values(by="jp_sales", ascending=False) 
        elif param == "pal_sales":
            dataset = dataset.sort_values(by="pal_sales", ascending=False) 
        elif param == "release_date":
            dataset = dataset.sort_values(by="release_date", ascending=False)    
        elif param == "last_update":
            dataset = dataset.sort_values(by="last_update", ascending=False)
        else:
            print("invalid input please enter one of the following parameters from above")
        return dataset    
            
    #get the amout of elemant you want the type of info and a dataset
    #retrun a dataframe at the same size by the required data from the dataset
    @staticmethod
    def get_data(size,info,dataset:pd.DataFrame):
        sorted_data = Data.sort_data(info,dataset)
        new_data = sorted_data[:size]
        return new_data
    
    
    #return the number of sales of a company
    @staticmethod
    def get_sum_of_sales(publisher, dataset:pd.DataFrame):
        company_data = dataset[dataset['publisher'] == publisher]
        sum = company_data['total_sales'].sum()
        return sum
    
    
    #how many games certain company published on a certain year
    @staticmethod
    def sold_in_year(year,company,dataset:pd.DataFrame):
        company_data = dataset[dataset['publisher'] == company]
        year_data = pd.to_datetime(company_data['release_date'], errors='coerce').dt.year
        new_dataset = company_data[year_data == year]
        num_of_games = len(new_dataset)
        return num_of_games
    
    
    #get the top n rows by total_sales
    @staticmethod
    def get_top_n_sales(n, dataset:pd.DataFrame):
        sorted_data = Data.sort_data("total_sales",dataset)
        new_dataset = sorted_data[:n]
        return new_dataset
    
    #Calculates the average critic score for games by a specific publisher
    @staticmethod
    def avg_critic_score(publisher, dataset:pd.DataFrame):
        publisher_data = dataset[dataset['publisher'] == publisher]
        avg = publisher_data['critic_score'].fillna(0).mean()
        return avg
    
    #Counts how many games belong to each genre
    @staticmethod
    def count_by_genre(dataset:pd.DataFrame):
        count = dataset['genre'].value_counts()        
        return count
    
    
    #convert sales amout to millions
    @staticmethod
    def to_millions(column, dataset:pd.DataFrame):
        if column not in ("critic_score", "total_sales", "na_sales", "jp_sales", "pal_sales","other_sales"):
            print("invalid column to convert to millions")
            return
        
        dataset[column] = dataset[column].mul(1000000)
        return dataset
    
    
    #how many games belong to each company
    @staticmethod
    def company_games(dataset:pd.DataFrame):
        count = dataset['publisher'].value_counts()
        return count
    
    #Returns all games released on a specific platform.
    @staticmethod
    def games_on_platforms(platform, dataset:pd.DataFrame):
        console = dataset[dataset['console'] == platform]
        count = len(console)
        return count
    
    #remove duplicate rows
    @staticmethod
    def remove_dup(dataset:pd.DataFrame):
        new_dataset = dataset.drop_duplicates()
        return new_dataset
    
    #Ensure columns are stored in the correct format
    @staticmethod
    def correct_foramat(dataset:pd.DataFrame):
        dataset['title'] = dataset['title'].astype(str)
        dataset['console'] = dataset['console'].astype(str)
        dataset['genre'] = dataset['genre'].astype(str)
        dataset['publisher'] = dataset['publisher'].astype(str)
        dataset['developer'] = dataset['developer'].astype(str)
        dataset['critic_score'] = pd.to_numeric(dataset['critic_score'], errors='coerce')
        dataset['total_sales'] = pd.to_numeric(dataset['total_sales'], errors='coerce')
        dataset['na_sales'] = pd.to_numeric(dataset['na_sales'], errors='coerce')
        dataset['jp_sales'] = pd.to_numeric(dataset['jp_sales'], errors='coerce')
        dataset['pal_sales'] = pd.to_numeric(dataset['pal_sales'], errors='coerce')
        dataset['other_sales'] = pd.to_numeric(dataset['other_sales'], errors='coerce')
        dataset['release_date'] = pd.to_datetime(dataset['release_date'], errors='coerce')
        dataset['last_update'] = pd.to_datetime(dataset['last_update'], errors='coerce')
        
        
    
    #Make sure similar data entries are identical
    @staticmethod
    def normalaiz_text(dataset:pd.DataFrame):
        for item in ["title","console","genre","publisher","developer"]:
            dataset[item] = dataset[item].str.upper()
            dataset[item] = dataset[item].str.strip()
            
    
    #return every year how many games released
    @staticmethod
    def release_in_year(dataset:pd.DataFrame):
        dataset['release_year'] = pd.to_datetime(dataset['release_date'], errors='coerce').dt.year
        released_by_year = dataset['release_year'].value_counts()
        return released_by_year

    #return the n top publishers with the highest total sales
    @staticmethod
    def get_top_publisher_salse(n, dataset:pd.DataFrame):
        grouped_data = dataset.groupby("publisher")["total_sales"].sum()
        sorted_data = grouped_data.sort_values(ascending=False)
        top_n = sorted_data.head(n)
        return top_n
    
    
    