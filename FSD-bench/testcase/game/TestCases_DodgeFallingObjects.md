### Black Box Unit Test Cases  

#### Functionality 1. Player Movement
- **Step**: Start the game and press the left arrow key.  
  **Expectation**: The player character moves to the left within the game area.  
- **Step**: Press the right arrow key.  
  **Expectation**: The player character moves to the right within the game area.  
- **Step**: Attempt to move the player character beyond the left edge of the screen.  
  **Expectation**: The player character does not move beyond the left edge.  
- **Step**: Attempt to move the player character beyond the right edge of the screen.  
  **Expectation**: The player character does not move beyond the right edge.  

#### Functionality 2. Collision Detection
- **Step**: Start the game and allow a block to fall until it collides with the player character.  
  **Expectation**: The game ends, and the final score is displayed.  
- **Step**: Move the player character to avoid a falling block.  
  **Expectation**: The player character successfully avoids the block, and the game continues.  

#### Functionality 3. Falling Blocks Behavior
- **Step**: Start the game and observe the falling blocks.  
  **Expectation**: Blocks appear randomly from the top of the screen and fall straight down.  
- **Step**: Survive for a period of time and observe the speed of falling blocks.  
  **Expectation**: The speed of the falling blocks increases as time progresses.  

#### Functionality 4. Scoring System
- **Step**: Start the game and survive for a few seconds.  
  **Expectation**: The score increases based on the time survived.  
- **Step**: End the game by colliding with a block.  
  **Expectation**: The final score is displayed, reflecting the total time survived.  

#### Functionality 5. Player Movement Constraints
- **Step**: Start the game and attempt to move the player character vertically using the arrow keys.  
  **Expectation**: The player character does not move vertically and remains at the bottom of the screen.  
- **Step**: Move the player character left and right while a block is falling.  
  **Expectation**: The player character can only move left or right, not vertically.  

#### Functionality 6. Game Over Condition
- **Step**: Start the game and allow the player character to collide with a falling block.  
  **Expectation**: The game ends immediately, and the final score is displayed.  
- **Step**: Restart the game after a game over.  
  **Expectation**: The game resets, and the player can start again from the beginning.  

#### Functionality 7. Data Storage
- **Step**: Play the game and achieve a score.  
  **Expectation**: The score is saved to a local text file upon game over.  
- **Step**: Check the local text file after a game session.  
  **Expectation**: The final score is correctly recorded in the text file.  