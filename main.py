import random
import logging
from typing import List


# configuration of logging the results to a file
logging.basicConfig(filename='reed_dice_game.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def ask_user() -> str:
    """
    Ask the user for how many time the simulation should run.

    Returns:
        str: A string base from the user input.
    """
    while True:
        user_input = input("Enter number of simulations: ")

        if user_input.strip().isdigit():
            return user_input

        print("\nEnter a valid number.")


def roll_dice() -> int:
    """
    Simulates rolling a single six-sided dice.

    Returns:
        int: A random number between 1 and 6.
    """
    return random.randint(1, 6)


def simulate_dice_game() -> List[int]:
    """
    Simulates a dice game according to the following rules:
    - If any number other than 1 or 6 is drawn, return the result immediately.
    - If 6 occurs twice, draw again and return all results up to 3 times.
    - If 1 occurs twice, draw again and return only the next valid draw
    (not including double 1's), up to 3 attempts.
    - If no valid result is obtained after 3 draws, return an empty list.

    Returns:
        List[int]: A list of dice results, or an empty list if no valid result
        is obtained.
    """
    results = []
    draw_count = 0

    while draw_count < 3:
        draw_1 = roll_dice()
        draw_2 = roll_dice()

        # if both draws are not 1 or 6 return immediately
        if draw_1 != 1 and draw_1 != 6 and draw_2 != 1 and draw_2 != 6:
            results.append(draw_1)
            results.append(draw_2)
            return results

        # if 6 occurs twice, draw again and return all results up to 3 times.
        if draw_1 == 6 and draw_2 == 6:
            draw_count = 0
            while draw_count < 3:
                results.append(roll_dice())
                results.append(roll_dice())
                draw_count += 1

            return results

        # in case of double 1's, continue drawing but don't return them
        # and don't add both 1s to result, then return the next valid results
        if draw_1 == 1 and draw_2 == 1:
            draw_count += 1
            continue

    # if no valid result is obtained in 3 draws, return an empty list
    return []


def main(num_simulations: int):
    """
    Runs the dice game simulation for a specified number of times and logs the
    results.

    Args:
        num_simulations (int): The number of times to run the dice game
        simulation.
    """
    for i in range(num_simulations):
        result = simulate_dice_game()
        logging.info(f"Simulation {i + 1}: {result}")
        print(f"Simulation {i + 1}: {result}")


if __name__ == "__main__":
    print("Welcome to Reed Dice Game Simulation")

    try:
        num_simulations = int(ask_user())
    except ValueError as e:
        raise e

    main(num_simulations)
