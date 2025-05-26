### Black Box Unit Test Cases

#### Functionalities 1. Player Movement
- **Step**: Move the player in the upward direction using the appropriate key.  
  **Expectation**: The player’s position on the grid updates correctly unless blocked by an obstacle.

#### Functionalities 2. Enemy Movement
- **Step**: Allow an enemy to move toward the player.  
  **Expectation**: The enemy's position updates based on its movement logic, correctly navigating around obstacles.

#### Functionalities 3. Bomb Placement
- **Step**: Press the space bar to place a bomb in an empty cell.  
  **Expectation**: The bomb is placed in the intended cell and is visually represented on the grid.

#### Functionalities 4. Bomb Explosion
- **Step**: Wait for the bomb to explode after the specified delay.  
  **Expectation**: The explosion occurs, extending fire in all four directions up to three squares, and the fire is blocked by obstacles.

#### Functionalities 5. Health Loss from Enemy Collision
- **Step**: Move the player directly into an enemy.  
  **Expectation**: The player’s health decreases appropriately, indicating damage from the enemy.

#### Functionalities 6. Health Loss from Bomb Explosion
- **Step**: Place a bomb near the player's current position and allow it to explode.  
  **Expectation**: The player's health decreases accordingly if they are within the blast radius.

#### Functionalities 7. Enemy Defeat
- **Step**: Inflict enough damage on an enemy to reduce its health to 0.  
  **Expectation**: The enemy disappears from the grid, and the player's score increases by 100.

#### Functionalities 8. Player Victory Conditions
- **Step**: Defeat all enemies on the grid.  
  **Expectation**: A victory message appears, displaying the player’s final score.

#### Functionalities 9. Player Loss Condition
- **Step**: Reduce the player's health to 0.  
  **Expectation**: A loss message is displayed, indicating that the player has been defeated.

#### Functionalities 10. Score Initialization
- **Step**: Start a new game session.  
  **Expectation**: The player's score is initialized to 0.