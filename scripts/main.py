'''
Liam O'Connor
Dec 13st, 2023
CS5001 Final Project
Steam Player Count Dashboard: main.py

This file contains the main function for the Steam Player Count Dashboard.
Required files: data/rawData/games.csv, data_processsing.py, data_fetch.py, visualization.py
'''
from data_fetch import fetch_current_player_count
from data_processing import read_player_count_csv, get_available_games
from visualization import plot_player_count

def main():
    while True:
        choice = input("Enter 'historical' for historical player count or 'current' for current player count: ").lower() # Get user input and convert to lowercase

        if choice == 'historical': # If they want to see all historical data (CSV Call)...
            available_games = get_available_games()
            print("Available games for historical data:") 
            print(available_games.to_string(index=False)) # Print from get_available_games() function (CSV file)
            
            game_id = input("Enter the game ID to visualize historical player count: ")
            player_count_data = read_player_count_csv(game_id)
            
            if player_count_data is not None:
                plot_player_count(player_count_data) # Plot the player count data
                break
            else:
                print(f"No historical data found for game ID {game_id}.")

        elif choice == 'current': # If they want to see current player count (API Call)...
            available_games = get_available_games()
            print("Available games for current player data:")
            print(available_games.to_string(index=False)) # Print from available_games function so they can see the game ID to input
            
            # Get current player count
            game_id = input("Enter the game ID number from the list above or another you might know: ")
            if not game_id.isdigit():
                print("Invalid game ID. The game ID must be numeric value.") # numeric check since game ID is a number (just bulletproofing)
                continue 

            game_name, count = fetch_current_player_count(game_id)
            
            if game_name and count is not None:
                print(f"There are {count} players online in {game_name} (ID: {game_id})")
                break
            else:
                print("Failed to fetch current player count or game ID is not valid.")


        else:
            print("Invalid choice. Please enter 'historical' or 'current'.")

if __name__ == "__main__":
    main()
