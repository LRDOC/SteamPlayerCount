'''
Liam O'Connor
Dec 13st, 2023
CS5001 Final Project
Steam Player Count Dashboard: visualization.py

This file contains the functions for visualizing data from the CSV files.
Required files: data/rawData/games.csv
'''

import matplotlib.pyplot as plt

def plot_player_count(data):
    ## TODO: rolling pandas.rolling
    '''
    This function plots the player count over time for the given game.
    
    Parameters: data (DataFrame): The DataFrame containing the player count data
    Returns: None
    '''
    plt.figure(figsize=(14, 7)) # Set the figure size to 14x7 inches
    plt.plot(data['Date'], data['Player Count'], marker='o') # Plot the data for the highest player count per month
    plt.plot(data['Date'], data['Player Count'].rolling(7).mean(), marker='o') # Plot the rolling average | Thank you Marcus for suggestion
    plt.title(f"Player Count Over Time for {data['Game Name'].iloc[0]}") # Set the title
    plt.xlabel("Date") # Set the x-axis label
    plt.ylabel("Player Count") # Set the y-axis label
    plt.xticks(rotation=45) # Rotate the x-axis tick labels by 45 degrees
    plt.tight_layout() # Automatically adjust the padding between the plot and the edges of the figure
    plt.legend(loc='upper left', labels=['Highest Player Count per Month', '30-Day Rolling Average']) # Add a legend to the plot (upper left corner
    plt.show() # Display the plot
