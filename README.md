# US States Guessing Game

This project is a fun and interactive game where players can guess the names of all 50 U.S. states. The game utilizes the Turtle graphics library for visual representation and provides an engaging way to learn U.S. geography.

## Features

- The game displays a blank map of the United States, where players can guess the names of the states.
- The current score is shown, along with the number of correct guesses.
- Players can exit the game at any time, which will save the names of any states they did not guess to a CSV file.
- The game updates the map dynamically as players guess the states correctly.

## Files

- **main.py**: This is the main program file that contains the logic for the game, including input handling, scoring, and visual updates on the map.
- **50_states.csv**: This CSV file contains the names of all 50 states and their respective coordinates for displaying on the map.
- **blank_states_img.gif**: This image file serves as the background for the game, showing a blank map of the United States.

## How to Run

To run the U.S. States Guessing Game, follow these steps:

1. Ensure you have Python and the necessary libraries installed (turtle and pandas).
2. Download the `main.py`, `50_states.csv`, and `blank_states_img.gif` files.
3. Open a terminal or command prompt and navigate to the directory containing the files.
4. Run the program using the following command:

   ```bash
   python main.py
   ```

5. Follow the on-screen instructions to guess the states.
6. To exit the game, type "exit," and your unguessed states will be saved to `states_to_learn.csv`.

## Enjoy the Game!

Test your knowledge of U.S. geography and have fun guessing all the states!