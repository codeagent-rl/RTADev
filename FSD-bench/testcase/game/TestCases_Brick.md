### Black Box Unit Test Cases  

#### Functionalities 1. Control Paddle Movement  
- **Step**: Press the left arrow key to move the paddle left.  
  **Expectation**: The paddle position is updated to the left on the screen.  

#### Functionalities 2. Ball Bounce Mechanics  
- **Step**: Launch the ball from the center and hit the paddle.  
  **Expectation**: The ball's trajectory changes and moves upward after bouncing off the paddle.  

#### Functionalities 3. Brick Splitting Logic  
- **Step**: Hit a brick with 3 lives using the ball.  
  **Expectation**: The brick splits into two smaller bricks, each with 2 lives remaining.  

#### Functionalities 4. Brick Disappearance  
- **Step**: Hit a brick multiple times until its life reaches 0.  
  **Expectation**: The brick disappears from the screen after its life counter reaches 0.  

#### Functionalities 5. Game Start Mechanism  
- **Step**: Press the left or right arrow key to start the game.  
  **Expectation**: The game starts successfully, and the ball is launched from the center of the window.  

#### Functionalities 6. Ball Movement  
- **Step**: Allow the ball to move upwards after being launched.  
  **Expectation**: The ball continuously moves upward until it collides with a brick or the paddle.  

#### Functionalities 7. Save Game State  
- **Step**: Pause the game and invoke the save function.  
  **Expectation**: The current game state is saved successfully to a local text file.  

#### Functionalities 8. Load Game State  
- **Step**: Load a previously saved game state.  
  **Expectation**: The game resumes from the saved state correctly, with all elements (paddle, ball, bricks) in their correct positions.  

#### Functionalities 9. End Game Condition  
- **Step**: Allow the ball to fall below the paddle.  
  **Expectation**: The game ends, and a game-over screen is displayed.  