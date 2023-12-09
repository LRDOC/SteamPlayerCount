'''
Liam O'Connor
Dec 13st, 2023
CS5001 Final Project
test_data_processing.py

This file contains the unit tests for the test_data_processing.py file.
'''
import unittest
from data_processing import get_available_games, read_player_count_csv

class TestDataProcessing(unittest.TestCase):

    def test_get_available_games(self):
        games = get_available_games()
        self.assertIsNotNone(games)

    def test_read_player_count_csv(self):
        # Example test (this requires a valid game ID and CSV file)
        game_id = '440'  # Team Fortress 2 
        data = read_player_count_csv(game_id)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
