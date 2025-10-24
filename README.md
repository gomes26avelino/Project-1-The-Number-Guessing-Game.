Number Guessing Game
A simple Python game where you guess a random number between 1 and 100. The computer gives you hints until you figure it out.
What it does
The game picks a number, you guess, and it tells you if you need to go higher or lower. When you finally get it, it shows how many tries it took. If you beat your previous best, it saves that as your new record.
I built this when I was learning Python fundamentals like loops, conditionals, and file handling. It's a classic beginner project, but it's actually pretty satisfying to play.
How it works

Random number gets picked (1-100)
You make a guess
Game tells you "higher" or "lower"
Repeat until you win
Your best score (fewest attempts) gets saved to a file
Play again or quit

Features

Handles bad input without crashing
Saves your high score between sessions
Simple hint system to guide you
Replay option without restarting the program
Works in any terminal

Running it
Clone and run:
bashgit clone https://github.com/gomes26avelino/number-guessing-game.git
cd number-guessing-game
python guessing_game.py
That's it. No dependencies, no setup.
What I learned

Working with Python's random module
Reading and writing files for persistent data
Basic error handling with try/except
Input validation
Keeping a game loop running smoothly

Notes

The high score file (high_score.txt) gets created automatically
If the file gets corrupted or deleted, the game just resets the record to 100
Uses recursion to restart the game, which is probably not the best approach for infinite replays, but works fine for casual use

Nothing fancy, just a functional little game. Fork it if you want to add features or use it to practice Python basics.
