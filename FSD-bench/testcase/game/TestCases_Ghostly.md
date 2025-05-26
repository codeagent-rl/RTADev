### Black Box Unit Test Cases  

#### Functionalities 1. Control the Ghost Movement  
- **Step**: Press the up arrow key to move the ghost.  
  **Expectation**: The ghost's position updates accordingly on the screen, moving one unit up unless blocked by a wall.  

#### Functionalities 2. Collision with Walls  
- **Step**: Move the ghost towards a wall using the arrow keys.  
  **Expectation**: The ghost does not pass through the wall and remains in its original position.  

#### Functionalities 3. Eating Pellets  
- **Step**: Move the ghost to collide with a pellet on the game field.  
  **Expectation**: The pellet is "eaten," removed from the game field, and the ghost's score or state updates accordingly.  

#### Functionalities 4. Eating Superpellets  
- **Step**: Move the ghost to collide with a superpellet on the game field.  
  **Expectation**: The superpellet is "eaten," removed from the game field, and the ghost gains the ability to eat other ghosts.  

#### Functionalities 5. Ghost Collision with Superpellet Power-up  
- **Step**: Move the ghost into another ghost while powered by a superpellet.  
  **Expectation**: The other ghost is "eaten" and disappears from the game, increasing the player's score.  

#### Functionalities 6. Invalid Move Collision  
- **Step**: Move the ghost towards another ghost without the power-up active.  
  **Expectation**: The ghost remains in its current position, and a message or indicator shows the move is invalid.  

#### Functionalities 7. Activation of the Monster  
- **Step**: Let the game run for 50 game ticks.  
  **Expectation**: After 50 ticks, a monster is activated and appears at position [1,1] on the screen.  

#### Functionalities 8. Monster Collision with Player’s Ghost  
- **Step**: Move the monster to collide with the player's ghost during gameplay.  
  **Expectation**: The game ends, and a game over message appears on the screen.  

#### Functionalities 9. End of Game Conditions  
- **Step**: Have the player's ghost collide with another ghost without the superpellet activated.  
  **Expectation**: The game ends, and a game over message appears, indicating the reason for the end condition.  