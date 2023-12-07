import matplotlib.pyplot as plt

def plot_player_count(data):
    '''
    This function plots the player count over time for the given game.
    
    Parameters: data (DataFrame): The DataFrame containing the player count data
    Returns: None
    '''
    plt.figure(figsize=(14, 7)) # Set the figure size to 14x7 inches
    plt.plot(data['Date'], data['Player Count'], marker='o') # Plot the data
    plt.title(f"Player Count Over Time for {data['Game Name'].iloc[0]}") # Set the title
    plt.xlabel("Date") # Set the x-axis label
    plt.ylabel("Player Count") # Set the y-axis label
    plt.xticks(rotation=45) # Rotate the x-axis tick labels by 45 degrees
    plt.tight_layout() # Automatically adjust the padding between the plot and the edges of the figure
    plt.show() # Display the plot
