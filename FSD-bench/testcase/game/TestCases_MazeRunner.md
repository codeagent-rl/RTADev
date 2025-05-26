### Black Box Unit Test Cases  

#### Functionality 1. Player Controls Character
- **Step**: Start the game and focus on the maze.  
- **Step**: Press the "up" arrow key.  
  **Expectation**: The character moves one step up in the maze, provided there is no obstacle.  
- **Step**: Press the "down" arrow key.  
  **Expectation**: The character moves one step down in the maze, provided there is no obstacle.  
- **Step**: Press the "left" arrow key.  
  **Expectation**: The character moves one step left in the maze, provided there is no obstacle.  
- **Step**: Press the "right" arrow key.  
  **Expectation**: The character moves one step right in the maze, provided there is no obstacle.  

#### Functionality 2. Maze Navigation and Obstacles
- **Step**: Start a level with a maze layout.  
- **Step**: Attempt to move the character into an obstacle.  
  **Expectation**: The character does not move and remains in the same position.  
- **Step**: Navigate through the maze to reach the exit.  
  **Expectation**: The character successfully reaches the exit if the path is clear, and the level is completed.  

#### Functionality 3. Collecting Stars
- **Step**: Start a level with stars placed in the maze.  
- **Step**: Move the character to collect a star.  
  **Expectation**: The star is collected, and the score increases by the designated points for that star.  
- **Step**: Collect multiple stars in one level.  
  **Expectation**: The score reflects the total points from all collected stars.  

#### Functionality 4. Multiple Levels with Increasing Difficulty
- **Step**: Complete the first level of the maze.  
- **Step**: Proceed to the next level.  
  **Expectation**: The next level features a larger maze with more complex paths and additional obstacles.  
- **Step**: Complete the second level.  
  **Expectation**: The player is able to access a third level that is even more challenging.  

#### Functionality 5. Strategic Movement and Dead Ends
- **Step**: Start a level with known dead ends.  
- **Step**: Attempt to navigate towards a dead end.  
  **Expectation**: The player realizes they are at a dead end and must backtrack to find the correct path.  
- **Step**: Successfully navigate through the maze without hitting dead ends.  
  **Expectation**: The player reaches the exit efficiently, demonstrating strategic movement.  

#### Functionality 6. Timer for Level Completion
- **Step**: Start a level and complete it.  
- **Expectation**: The timer stops upon reaching the exit, and the time taken is displayed.  
- **Step**: Replay the same level.  
  **Expectation**: The timer tracks the new completion time, allowing the player to compare it with the previous attempt.  

#### Functionality 7. Progress Tracking
- **Step**: Complete multiple levels in the game.  
- **Expectation**: The game records the completion times for each level in local storage.  
- **Step**: Check the progress report.  
  **Expectation**: The report displays the completion times and levels completed accurately.  

#### Functionality 8. Scoring System
- **Step**: Complete a level while collecting stars and tracking moves.  
- **Expectation**: The score is calculated based on completion time, stars collected, and the number of moves made.  
- **Step**: Compare scores after completing the same level multiple times.  
  **Expectation**: The scores reflect the player's performance, showing improvements or declines based on the criteria.  