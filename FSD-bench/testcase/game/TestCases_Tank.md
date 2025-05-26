### Black Box Unit Test Cases  

#### Functionalities 1. Move Player's Tank  
- **Step**: Press the up arrow key to move the player's tank one step up.  
  **Expectation**: The player's tank moves one cell up on the grid, and its new position is updated accordingly.  

#### Functionalities 2. Fire Bullet  
- **Step**: Press the 'Enter' key to fire a bullet.  
  **Expectation**: A bullet is displayed moving in the direction of the player's tank, and the bullet's position updates accordingly.  

#### Functionalities 3. Hit Enemy Tank  
- **Step**: The bullet successfully collides with an enemy tank.  
  **Expectation**: The enemy tank's health decreases by 100 points, and if health reaches zero, the tank is marked as destroyed and the player’s score increases by 200 points.  

#### Functionalities 4. Player Tank Gets Hit  
- **Step**: An enemy tank successfully shoots the player's tank.  
  **Expectation**: The player's tank health decreases by 10 points. If health reaches zero, the player's tank is marked as destroyed.  

#### Functionalities 5. Check Game End Conditions  
- **Step**: All enemy tanks are destroyed.  
  **Expectation**: The game ends and displays the player's final score.  

#### Functionalities 6. Check Score Calculation  
- **Step**: Destroy an enemy tank and retrieve the player's score.  
  **Expectation**: The player's score increases by 200 points for each enemy tank destroyed.  

#### Functionalities 7. Load Game Data  
- **Step**: Load saved game data from a local text file containing tank positions and health.  
  **Expectation**: The game state is restored to the positions and health as indicated in the file without errors.  

#### Functionalities 8. Store Game Data  
- **Step**: Save the current game state to a local text file.  
  **Expectation**: The game state is successfully written to the file without data loss or corruption.  

#### Functionalities 9. Check Grid Boundaries  
- **Step**: Attempt to move the player's tank outside the 20x20 grid boundary.  
  **Expectation**: The tank does not move outside the boundaries, and its position remains unchanged.  