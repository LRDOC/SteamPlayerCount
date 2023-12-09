'''
Liam O'Connor
Dec 13st, 2023
CS5001 Final Project
test_data_fetch.py

This file contains the unit tests for the test_data_fetch.py file.
'''
import unittest
from data_fetch import fetch_current_player_count

class TestDataFetch(unittest.TestCase):

    def test_fetch_current_player_count(self):
        # Example test (bc requires a valid game ID)
        game_id = '440'  # Team Fortress 2 for example
        game_name, count = fetch_current_player_count(game_id)
        self.assertIsNotNone(game_name)
        self.assertIsInstance(count, int)

if __name__ == '__main__':
    unittest.main()
