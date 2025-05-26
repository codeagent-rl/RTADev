### Black Box Unit Test Cases  

#### Functionality 1. Navigate the Maze
- **Step**: Start the game and observe the initial maze layout.  
  **Expectation**: The maze is displayed with walls and paths, and the player character is positioned at the starting point.  
- **Step**: Use the arrow keys to move the character up, down, left, and right.  
  **Expectation**: The character moves accordingly without passing through walls.

#### Functionality 2. Find the Treasure
- **Step**: Start a new game and navigate through the maze.  
- **Step**: Reach the treasure location.  
  **Expectation**: The game recognizes the treasure has been found, and the player is notified with a success message.

#### Functionality 3. Score Tracking
- **Step**: Successfully find the treasure in the maze.  
  **Expectation**: The player's score increases by a predefined amount.  
- **Step**: Find the treasure again in a new maze.  
  **Expectation**: The score continues to increase with each successful treasure find.

#### Functionality 4. Timer Implementation
- **Step**: Start a new game and observe the timer.  
  **Expectation**: The timer starts counting down as soon as the game begins.  
- **Step**: Find the treasure before the timer runs out.  
  **Expectation**: The game records the time taken to find the treasure and displays it.

#### Functionality 5. Level Progression
- **Step**: Find the treasure in the first maze.  
  **Expectation**: The player is transported to a new, more complex maze.  
- **Step**: Attempt to find the treasure in the new maze.  
  **Expectation**: The player can navigate the new maze with additional obstacles.

#### Functionality 6. Game Over Condition
- **Step**: Start a new game and allow the timer to run out without finding the treasure.  
  **Expectation**: The game ends, and a game over message is displayed.  
- **Step**: Attempt to continue playing after the game over message.  
  **Expectation**: The game does not allow further actions until restarted.

#### Functionality 7. Best Time Storage
- **Step**: Complete a level and record the time taken.  
  **Expectation**: The time is saved as the player's best time if it is the fastest recorded.  
- **Step**: Restart the game and complete the level again with a slower time.  
  **Expectation**: The best time remains unchanged.

#### Functionality 8. Restart Game Option
- **Step**: Finish a level or reach game over.  
- **Step**: Select the option to restart the game.  
  **Expectation**: The game resets to the initial state, allowing the player to start over.  
- **Step**: Navigate through the maze after restarting.  
  **Expectation**: The maze is generated anew, and the player can begin the hunt for treasure again.