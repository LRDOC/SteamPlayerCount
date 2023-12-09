'''
Liam O'Connor
Dec 13st, 2023
CS5001 Final Project
Steam Player Count Dashboard: data_processing.py

This file contains the functions for processing data from the Steam Web API and CSV files. 
Required files: data/rawData/games.csv
'''

import pandas as pd
import os

def get_available_games(csv_filename='games.csv'): 
    '''
    This function reads the CSV file and returns a DataFrame containing the game names and IDs.
    
    Parameters: csv_filename (str): The name of the CSV file to read from
    Returns: df (DataFrame): The DataFrame containing the game names and IDs
    '''
    # This should navigate up one directory from 'scripts' to the project root
    project_root = os.path.dirname(os.path.dirname(__file__)) # os.path.dirname(__file__) returns the path to the current file
    
    # construct the path to 'data/rawData/games.csv' using os.path.join() because this is submitted and majority of ppl have macs :)
    csv_path = os.path.join(project_root, 'data', 'rawData', csv_filename) # /~/VideoGamePopularityAnalysis/data/rawData/games.csv
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"The file {csv_path} does not exist.")
    
    df = pd.read_csv(csv_path)
    return df[['Game Name', 'game_id']].drop_duplicates() # Return only the 'Game Name' and 'game_id' columns and drop duplicate rows

def read_player_count_csv(game_id, csv_filename='games.csv'):
    '''
    This function reads the player count data from the CSV file and returns a DataFrame
    containing the player count data for the given game_id.
    If the game_id is not found in the CSV file, this function returns None.
    
    Parameters: game_id (str): The game ID to filter the DataFrame for
                csv_filename (str): The name of the CSV file to read from
    Returns: df (DataFrame): The DataFrame containing the player count data for the given game_id
    '''
    project_root = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(project_root, 'data', 'rawData', csv_filename)
    
    if not os.path.exists(csv_path): # Check if the file exists (IT SHOULD EXIST BC SINCE WE ARE READING FROM IT AND ITS DOWNLOADED????)
        raise FileNotFoundError(f"The file {csv_path} does not exist.") #This error should never be raised unless i messed up
    
    df = pd.read_csv(csv_path)
    df['game_id'] = df['game_id'].astype(str) # Convert the 'game_id' column to string type because the input parameter is a string
    game_id = str(game_id) # convert game_id to string | quality of life change
    
    # Dataframes are immutable so we need to assign the filtered dataframe to a new variable
    df = df[df['game_id'] == game_id] # Filter the dataframe to only include rows where the 'game_id' column matches the given game_id
    
    if df.empty: # If the dataframe is empty, return None
        return None
    
    df['Date'] = pd.to_datetime(df['Date'])  # Convert the 'Date' column to datetime format
    return df
