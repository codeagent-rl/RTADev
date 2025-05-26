### Black Box Unit Test Cases  

#### Functionality 1. Navigate Through the Maze
- **Step**: Start the game and load the first maze level.  
- **Step**: Attempt to slide a tile horizontally to create a path.  
  **Expectation**: The tile moves successfully, and the maze layout updates to reflect the new configuration.  
- **Step**: Slide a tile vertically to create a path.  
  **Expectation**: The tile moves successfully, and the maze layout updates to reflect the new configuration.  

#### Functionality 2. Objective of Reaching the Exit Tile
- **Step**: Start the game and navigate the player character through the maze.  
- **Step**: Move the player character to the exit tile.  
  **Expectation**: The game recognizes that the player has reached the exit tile and displays a success message.  
- **Step**: Attempt to move the player character into a wall or obstacle.  
  **Expectation**: The game prevents the movement and displays a message indicating that the move is not allowed.  

#### Functionality 3. Multiple Levels with Increasing Difficulty
- **Step**: Start the game and select the first level.  
- **Expectation**: The first level loads with a simple maze layout.  
- **Step**: Complete the first level and proceed to the second level.  
- **Expectation**: The second level loads with a more complex maze layout and additional obstacles.  

#### Functionality 4. Timer Tracking
- **Step**: Start a new game and load a maze level.  
- **Expectation**: A timer starts counting down as soon as the player begins to navigate the maze.  
- **Step**: Complete the maze and check the timer.  
  **Expectation**: The timer stops, and the total time taken to complete the maze is displayed.  

#### Functionality 5. Collecting Bonus Points
- **Step**: Start a maze level with stars scattered throughout.  
- **Step**: Move the player character to collect a star.  
  **Expectation**: The star is collected, and the player's score increases by the designated bonus points.  
- **Step**: Attempt to collect a star that is unreachable due to an obstacle.  
  **Expectation**: The game prevents the collection and displays a message indicating that the star cannot be reached.  

#### Functionality 6. Resetting the Maze
- **Step**: Start a maze level and make several moves.  
- **Step**: Click the reset button to restart the maze.  
  **Expectation**: The maze resets to its original configuration, and the player character returns to the starting point.  
- **Step**: Attempt to reset the maze after reaching the exit tile.  
  **Expectation**: The maze resets successfully, allowing the player to try again.  

#### Functionality 7. Choosing a Different Level
- **Step**: Start the game and complete the first level.  
- **Step**: Navigate to the level selection screen.  
- **Expectation**: The level selection screen displays available levels.  
- **Step**: Select a different level to play.  
  **Expectation**: The selected level loads successfully, and the player can begin navigating the new maze.  