### Black Box Unit Test Cases  

#### Functionality 1: Connect Numbers in Sequence
- **Step**: Start a new game with a 3x3 grid containing numbers 1 to 9.  
- **Step**: Click on the tile with number 1, then the tile with number 2, and continue clicking in numerical order up to 9.  
  **Expectation**: The path is successfully formed, and the game recognizes the sequence as valid.  

- **Step**: Start a new game with a 4x4 grid containing numbers 1 to 16.  
- **Step**: Click on the tile with number 1, then click on a non-adjacent tile with number 2.  
  **Expectation**: The game does not allow the move and displays an error message indicating that the move is invalid.  

#### Functionality 2: Movement Restrictions
- **Step**: Start a new game with a 5x5 grid.  
- **Step**: Click on the tile with number 1, then click on the tile with number 2 (adjacent).  
- **Step**: Click on the tile with number 3 (non-adjacent).  
  **Expectation**: The game does not allow the move to the non-adjacent tile and maintains the current path.  

- **Step**: Start a new game with a 4x4 grid.  
- **Step**: Click on the tile with number 1, then click on the tile with number 2, and continue to number 3.  
- **Step**: Click on the tile with number 2 again.  
  **Expectation**: The game does not allow revisiting the tile and displays an error message.  

#### Functionality 3: Continuous Path Requirement
- **Step**: Start a new game with a 3x3 grid.  
- **Step**: Click on the tile with number 1, then click on the tile with number 2, and then click on the tile with number 4 (skipping number 3).  
  **Expectation**: The game does not allow the move and indicates that the path is broken.  

- **Step**: Start a new game with a 4x4 grid.  
- **Step**: Click on the tile with number 1, then click on the tile with number 2, and then click on the tile with number 3.  
- **Step**: Click on the tile with number 5 (skipping number 4).  
  **Expectation**: The game does not allow the move and maintains the current path.  

#### Functionality 4: Multiple Levels with Increasing Difficulty
- **Step**: Start the game and select level 1 (3x3 grid).  
- **Expectation**: The game initializes with a 3x3 grid and numbers 1 to 9 displayed.  

- **Step**: Complete level 1 successfully.  
- **Step**: Start level 2.  
- **Expectation**: The game initializes with a 4x4 grid and numbers 1 to 16 displayed.  

#### Functionality 5: Timer Challenge
- **Step**: Start a new game with a 3x3 grid and note the timer starts.  
- **Step**: Complete the path from 1 to 9.  
- **Expectation**: The game displays the time taken to complete the path and whether it was completed within the time limit.  

- **Step**: Start a new game with a 4x4 grid and observe the timer.  
- **Step**: Take longer than the allowed time to complete the path.  
- **Expectation**: The game ends and displays a message indicating that the time limit has been exceeded.  

#### Functionality 6: Data Storage
- **Step**: Complete a game and save the score.  
- **Expectation**: The score is stored in a local text file.  

- **Step**: Restart the game and load the saved scores from the text file.  
- **Expectation**: The previously saved scores are displayed correctly in the game.  