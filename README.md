# Reed Dice Game Simulation

This application simulates a dice game where a six-sided die is rolled according to a set of rules, with the goal of collecting and evaluating the results over a series of simulations. The application logs the results of each simulation to a file and prints them to the console.

### How It Works

The dice game follows these rules:

1. Two dice are rolled.
2. If neither die is a 1 nor a 6, the result is returned immediately.
3. If both dice show 6, a new set of rolls is made up to three additional times, and all results are collected.
4. If both dice show 1, the game continues to roll the dice, ignoring double 1 rolls, until a valid result is obtained (up to three attempts).
5. If no valid result is obtained after three draws, an empty list is returned.

### Usage

**Running the Application**

1. Clone the repository to your local machine.
2. Ensure you have `Python 3.12` installed.
3. Run the `main.py` script:
```
python3 main.py
```
4. The program will ask you to input the number of simulations you want to run.
5. Results will be printed in the console and logged to the `reed_dice_game.log` file.

**Running Unit Tests**

To run the tests, you will need to use `unittest`:
1. In the root of the project directory, run the following command:
```
python3 -m unittest test_main.py
```
2. All tests will execute, and the results will be printed in the console.

### Logging

The results of each simulation are logged to a file called `reed_dice_game.log`. Each entry is timestamped and includes the simulation number and the result of that simulation. For example:
```
2024-09-28 18:34:10,522 - Simulation 1: [3, 5]
2024-09-28 18:34:12,123 - Simulation 2: []
```
To modify the log level or file format, adjust the `logging.basicConfig` configuration in `main.py`.
