# Lab 2: Number Guessing Game

## Instructions

In this lab, we will create a simple number guessing game. The program will choose a random number between 1 and 100. The user will then be asked to guess the number. If the user's guess is higher than the random number, the program will print out "Too high!". If the user's guess is lower than the random number, the program will print out "Too low!". If the user's guess is equal to the random number, the program will print out "You win!". The user will keep guessing until they guess the correct number. 

Once you have the loop added, we're going to add some more features! We'll keep count of how many guesses it took the user and print it out at the bottom. Once we have this, let's update the message to show the proper boundaries where the user can guess. For example, if the user guesses a number that's too high, the upper boundary should change in the output prompt.

## Example Outputs

```bash
Guess a number between 1 and 100: 50

Too high!

Guess a number between 1 and 50: 25

Too low!

Guess a number between 25 and 50: 37

Too high!

Guess a number between 25 and 37: 31

Too low!

Guess a number between 31 and 37: 34

You win!

It took you 5 guesses to solve it!

```

## Running the program

To run the program, type the following command in the terminal:

```bash
python3 number_guessing_game.py
```

*Note: If you're using Windows, you may need to use `python` instead of `python3`.*

## Extra Credit

1. [ ] \[+10\] After the program ends, ask the user if they want to play again. If they do, start the game over. If they don't, print out "Goodbye!" and end the program.
2. [ ] \[+20\] Draw the Pseudocode of the Program and upload it to your GitHub repository.

