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
                os.rename(data_file,"videoGame2024_dataset.csv")
            except FileNotFoundError:
                print(f"the dataset file not found")
            except Exception as e:
                print(f"an error occured {e}")
                
            data_set_frame = pd.read_csv("videoGame2024_dataset.csv")
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
            dataset.to_csv("videoGame2024_dataset", index= False)
        except Exception as e:
            print(f"exception {e} has occured")
        
    #sort the dataset by paarameter
    @staticmethod
    def dort_data(dataset:pd.DataFrame):
        param = input("choos a parameter to sort by him the data: console\n publisher\n developer\n critic_score\n total_sales\n na_sales\n  jp_sales\n pal_sales\n release_date\n last_update")
        if param == "console":
            dataset.sort_values(by="console", ascending=False, inplace=True)
        elif param == "publisher":
            dataset.sort_values(by="publisher", ascending=False, inplace=True)    
        elif param == "developer":
            dataset.sort_values(by="developer", ascending=False, inplace=True)
        elif param == "critic_score":
            dataset.sort_values(by="critic_score", ascending=False, inplace=True)    
        elif param == "total_sales":
            dataset.sort_values(by="total_sales", ascending=False, inplace=True)
        elif param == "na_sales":
            dataset.sort_values(by="na_sales", ascending=False, inplace=True) 
        elif param == "jp_sales":
            dataset.sort_values(by="jp_sales", ascending=False, inplace=True) 
        elif param == "pal_sales":
            dataset.sort_values(by="pal_sales", ascending=False, inplace=True) 
        elif param == "release_date":
            dataset.sort_values(by="release_date", ascending=False, inplace=True)    
        elif param == "last_update":
            dataset.sort_values(by="last_update", ascending=False, inplace=True)
        else:
            print("invalid input please enter one of the following parameters from above")
        return dataset    
            
    #get the amout of elemant you want the type of info and a dataset
    #retrun a dataframe at the same size by the required data from the dataset
    @staticmethod
    def get_data(self,size,info,dataset:pd.DataFrame):
        pass
        