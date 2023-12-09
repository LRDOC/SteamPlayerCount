'''
Liam O'Connor
Dec 13st, 2023
CS5001 Final Project
Steam Player Count Dashboard: data_fetch.py

This file contains the functions for fetching data from the Steam Web API.
Required: API key for Steam Web API
'''
import requests

api_key = '9258E8DCFB629F7B9B3A7A252C98ACA2'  # (private) API key for Steam Web API if you are reading this, dont steal my key pls

def fetch_current_player_count(game_id):
    player_count_url = f"http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={game_id}&key={api_key}"
    app_list_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/" #Thank you Steam Forums for this link.
    
    # Get current player count (API request)
    player_response = requests.get(player_count_url) # Make a GET request to the player count URL
    if player_response.status_code == 200: # If the request was successful...
        player_count = player_response.json()['response']['player_count'] # Get the player count
    else:
        return None, None

    # Get list of apps to find game name (API request and app list matching)
    app_list_response = requests.get(app_list_url)
    if app_list_response.status_code == 200: # If the request was successful...
        games_titles = app_list_response.json()['applist']['apps'] # Get the list of game titles
        game_name = None
        for app in games_titles: 
            if str(app['appid']) == str(game_id): # If the app ID matches the given game ID...
                game_name = app['name'] # Get the game name (please)
                break
        if game_name:
            return game_name, player_count # Return the game name and player count
        else:
            return "Game name not found", player_count # Return the player count and a message saying the game name was not found
    else:
        return None, None