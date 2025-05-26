# Software Description

## Objective

Develop a Bomberman Game

## Core Features

The game uses a 13x13 grid with obstacles placed on even-numbered rows and columns.
The player (green) and enemies (red) move on the grid, avoiding obstacles.
The player can place bombs using the space bar. Bombs explode after a short delay, spreading fire in all four directions for three squares.
Fire is blocked by obstacles.
The player starts with 100 health and a score of 0, while enemies start with 10 health.
The player loses health when colliding with enemies or being caught in explosions.
If an enemy's health reaches 0, it disappears, and the player’s score increases by 100.
The player loses if their health reaches 0 and wins if all enemies are defeated, displaying a victory message with the score.

## Language

Use python to develop a pygame application.

### Data Storage

Data will be stored in local text files.