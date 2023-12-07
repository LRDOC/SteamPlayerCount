import requests

api_key = '9258E8DCFB629F7B9B3A7A252C98ACA2'  # (private) API key for Steam Web API if you are reading this, dont steal my key pls

def fetch_current_player_count(game_id):
    '''
    This function fetches the current player count for the given game ID.
    If the game ID is not valid or the request fails, this function returns None.
    
    Parameters: game_id (str): The game ID to fetch the current player count for
    Returns: game_name (str): The name of the game
    '''
    url = f"http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={game_id}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200: # API- Request was successful
        data = response.json()
        player_count = data['response']['player_count'] # Get the player count from the response
        
        # TODO: Add functionality to get game name if possible, otherwise return None or a placeholder
        game_name = "Game Name Placeholder"  # Replace with actual game name retrieval method
        return game_name, player_count
    else:
        return None, None
