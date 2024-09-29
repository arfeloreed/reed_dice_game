import unittest
from unittest.mock import patch
from main import roll_dice, simulate_dice_game, ask_user, main


class TestReedDiceGame(unittest.TestCase):

    @patch('main.roll_dice')
    def test_roll_dice(self, mock_roll_dice):
        """
        Test that roll_dice returns a value between 1 and 6.
        """
        mock_roll_dice.return_value = 3
        result = roll_dice()
        self.assertIn(result, range(1, 7),
                      "dice roll should return a value between 1 and 6.")

    @patch('main.input', return_value='5')
    def test_ask_user_valid_input(self, mock_input):
        """
        Test that ask_user correctly returns valid input as string.
        """
        result = ask_user()
        self.assertEqual(result, '5',
                         "ask_user should return the user input as a string.")

    @patch('main.input', side_effect=['invalid', '10'])
    def test_ask_user_invalid_then_valid_input(self, mock_input):
        """
        Test that ask_user prompts again if the input is invalid, and
        eventually returns valid input.
        """
        result = ask_user()
        self.assertEqual(
            result, '10',
            "ask_user should return the valid user input after invalid input."
        )

    @patch('main.roll_dice')
    def test_simulate_dice_game_no_valid_result(self, mock_roll_dice):
        """
        Test that simulate_dice_game returns an empty list when no valid result
        is obtained after 3 draws.
        """
        # simulate rolling double 1's 3 times, so no valid result is obtained
        mock_roll_dice.side_effect = [1, 1, 1, 1, 1, 1]
        result = simulate_dice_game()
        self.assertEqual(
            result,
            [],
            "should return an empty list if no valid result is obtained."
        )

    @patch('main.roll_dice')
    def test_simulate_dice_game_valid_draw(self, mock_roll_dice):
        """
        Test that simulate_dice_game returns valid results when a valid draw
        is made.
        """
        # simulate rolling a 3 and a 4, which should return immediately
        mock_roll_dice.side_effect = [3, 4]
        result = simulate_dice_game()
        self.assertEqual(
            result,
            [3, 4],
            "Should return valid draws immediately if none of the special \
            cases occur."
        )

    @patch('main.roll_dice')
    def test_simulate_dice_game_double_6(self, mock_roll_dice):
        """
        Test that simulate_dice_game draws again when two 6's are rolled.
        """
        # simulate rolling double 6's, followed by three additional rolls
        mock_roll_dice.side_effect = [6, 6, 3, 4, 5, 2, 5, 3]
        result = simulate_dice_game()
        self.assertEqual(
            result,
            [3, 4, 5, 2, 5, 3],
            "should return three additional rolls after two 6's are rolled."
        )

    @patch('main.roll_dice')
    def test_simulate_dice_game_double_1(self, mock_roll_dice):
        """
        Test that simulate_dice_game skips double 1's and returns the next
        valid result.
        """
        # simulate rolling double 1's, followed by a valid result (3, 4)
        mock_roll_dice.side_effect = [1, 1, 3, 4]
        result = simulate_dice_game()
        self.assertEqual(
            result,
            [3, 4],
            "should skip double 1's and return the next valid result."
        )

    @patch('main.simulate_dice_game')
    @patch('main.logging.info')
    def test_main_simulation(self, mock_logging_info, mock_simulate_dice_game):
        """
        Test that main function runs the simulation and logs results.
        """
        mock_simulate_dice_game.return_value = [2, 3]
        main(3)  # Run the simulation 3 times

        self.assertEqual(
            mock_simulate_dice_game.call_count,
            3,
            "simulate_dice_game should be called 3 times."
        )

        self.assertEqual(
            mock_logging_info.call_count,
            3,
            "logging.info should be called 3 times."
        )
