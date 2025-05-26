# Software Description

## Objective

Develop a Ghostly game. You must design a GUI.

## Core Features

The player controls a ghost using the arrow keys.
The game features walls that the ghost cannot pass through.
The ghost can eat pellets and superpellets (big pellets), gaining special abilities.
Eating a superpellet allows the player’s ghost to eat other ghosts, causing them to disappear.
Colliding with another ghost without the superpellet power-up results in an invalid move, like hitting a wall.
After 50 game ticks, a monster is activated at position [1,1] to chase the player's ghost. If the monster collides with the player's ghost, the game ends.
The game ends if the player's ghost collides with a monster or another ghost without the power-up.

## Language

Use python to develop a pygame application.

### Data Storage

Data will be stored in local text files.
