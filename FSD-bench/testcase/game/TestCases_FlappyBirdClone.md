### Black Box Unit Test Cases  

#### Functionality 1. Bird Control
- **Step**: Start the game and observe the bird's initial position.  
  **Expectation**: The bird is positioned at the starting height and begins to fall due to gravity.  
- **Step**: Click the mouse or press any key to make the bird flap.  
  **Expectation**: The bird moves upward in response to the input.  

#### Functionality 2. Pipe Navigation
- **Step**: Start the game and observe the pipes appearing from the right side of the screen.  
  **Expectation**: Pipes are generated at regular intervals with a gap for the bird to pass through.  
- **Step**: Attempt to navigate the bird through the gap between the pipes.  
  **Expectation**: The bird successfully passes through the gap without colliding with the pipes.  

#### Functionality 3. Pipe Movement
- **Step**: Start the game and observe the pipes moving from right to left.  
  **Expectation**: Pipes move continuously from the right side of the screen to the left.  
- **Step**: Score points by passing through multiple sets of pipes.  
  **Expectation**: The speed of the pipes increases as the player scores more points.  

#### Functionality 4. Scoring System
- **Step**: Start the game and pass through the first set of pipes.  
  **Expectation**: The score increases by one point.  
- **Step**: Continue passing through additional sets of pipes.  
  **Expectation**: The score continues to increase with each successful pass.  

#### Functionality 5. Game Over Conditions
- **Step**: Start the game and collide with a pipe.  
  **Expectation**: The game ends, and the final score is displayed.  
- **Step**: Let the bird fall to the ground.  
  **Expectation**: The game ends, and the final score is displayed.  

#### Functionality 6. Restart Game
- **Step**: After the game ends, observe the option to restart.  
  **Expectation**: A restart button or option is available to the player.  
- **Step**: Click the restart button.  
  **Expectation**: The game resets, and the player can start a new game session.  

#### Functionality 7. High Score Storage
- **Step**: Play the game and achieve a score of 5 points.  
  **Expectation**: The score is saved in a local text file as the high score.  
- **Step**: Restart the game and achieve a score of 3 points.  
  **Expectation**: The high score remains at 5 points, and the new score of 3 points does not overwrite it.  