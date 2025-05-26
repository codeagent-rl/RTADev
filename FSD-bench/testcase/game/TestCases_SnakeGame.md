### Black Box Unit Test Cases  

#### Functionality 1. Control the Snake with Arrow Keys
- **Step**: Start the game and press the Up arrow key.  
  **Expectation**: The snake moves upward on the screen.  
- **Step**: Press the Down arrow key.  
  **Expectation**: The snake moves downward on the screen.  
- **Step**: Press the Left arrow key.  
  **Expectation**: The snake moves left on the screen.  
- **Step**: Press the Right arrow key.  
  **Expectation**: The snake moves right on the screen.  

#### Functionality 2. Eating Food
- **Step**: Start the game and allow the snake to move towards the food.  
  **Expectation**: When the snake collides with the food, the snake grows longer, and the food disappears.  
- **Step**: Check the score after eating food.  
  **Expectation**: The score increases by 1 for each piece of food consumed.  

#### Functionality 3. Avoiding Collisions
- **Step**: Move the snake towards the wall of the screen.  
  **Expectation**: The game ends, and a message indicating the game over is displayed.  
- **Step**: Move the snake to collide with its own body.  
  **Expectation**: The game ends, and a message indicating the game over is displayed.  

#### Functionality 4. Scoring System
- **Step**: Start the game and eat 5 pieces of food.  
  **Expectation**: The score displayed should be 5.  
- **Step**: Continue eating food until the score reaches 10.  
  **Expectation**: The score displayed should be 10, reflecting the total pieces of food eaten.  

#### Functionality 5. Increasing Difficulty
- **Step**: Start the game and eat food to grow the snake.  
  **Expectation**: As the snake grows longer, the player must navigate more carefully to avoid collisions.  
- **Step**: Observe the speed of the snake as it grows.  
  **Expectation**: The speed of the snake increases, making the game more challenging as the snake lengthens.  

#### Functionality 6. Pause and Resume Game
- **Step**: Start the game and press the pause button.  
  **Expectation**: The game pauses, and a pause menu displaying the current score and a restart option appears.  
- **Step**: Click the resume button on the pause menu.  
  **Expectation**: The game resumes from where it was paused.  

#### Functionality 7. Game Over and Final Score Display
- **Step**: End the game by colliding with a wall or the snake's body.  
  **Expectation**: The game ends, and the final score is displayed on the screen.  
- **Step**: Restart the game after viewing the final score.  
  **Expectation**: The game resets, and the score is set back to zero.  

#### Functionality 8. Data Storage
- **Step**: Play the game and achieve a score of 15.  
  **Expectation**: The score is saved in a local text file.  
- **Step**: Close and reopen the game.  
  **Expectation**: The previously saved score is loaded from the local text file and displayed.  