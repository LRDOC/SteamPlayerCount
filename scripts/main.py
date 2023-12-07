from data_fetch import fetch_current_player_count
from data_processing import read_player_count_csv, get_available_games
from visualization import plot_player_count

def main():
    choice = input("Enter 'historical' for historical player count or 'current' for current player count: ").lower()

    if choice == 'historical':
        # List the available games for which historical data can be visualized
        available_games = get_available_games()
        print("Available games for historical data:")
        print(available_games.to_string(index=False))  # Prints the DataFrame without the index
        
        # Ask the user to choose from available game IDs
        game_id = input("Enter the game ID to visualize historical player count: ")
        player_count_data = read_player_count_csv(game_id)
        
        if player_count_data is not None:
            # Plot the player count
            plot_player_count(player_count_data)
        else:
            print(f"No historical data found for game ID {game_id}.")

    elif choice == 'current':
        # List the available games for which historical data can be visualized
        available_games = get_available_games()
        print("Available games for historical data:")
        print(available_games.to_string(index=False))  # Prints the DataFrame without the index
        
        game_id = input("Enter the game ID number: ")# Ask the user to input the game ID
        game_name, count = fetch_current_player_count(game_id)# Fetch and display current player count
        
        # Display the current player count
        if game_name and count is not None: 
            print(f"{game_name} (ID: {game_id}): {count}")
        else:
            print("Failed to fetch current player count or game ID is not valid.")
    
    else:
        print("Invalid choice. Please enter 'historical' or 'current'.")

if __name__ == "__main__":
    main()
