### Black Box Unit Test Cases  

#### Functionality 1. Game Initialization
- **Step**: Launch the Tic-Tac-Toe game application.  
  **Expectation**: The game window opens with a 3x3 grid displayed, and the first player (X) is indicated to start.  

#### Functionality 2. Player Turn Alternation
- **Step**: Player X places an "X" in the top-left cell.  
- **Step**: Player O places an "O" in the center cell.  
- **Step**: Player X places an "X" in the top-center cell.  
  **Expectation**: The game alternates turns correctly, allowing Player X and Player O to place their symbols in the grid without any errors.  

#### Functionality 3. Check for a Winner
- **Step**: Player X places an "X" in the top-left cell.  
- **Step**: Player O places an "O" in the center cell.  
- **Step**: Player X places an "X" in the top-center cell.  
- **Step**: Player O places an "O" in the bottom-left cell.  
- **Step**: Player X places an "X" in the top-right cell.  
  **Expectation**: The game detects that Player X has formed a horizontal line at the top and displays a message indicating Player X has won.  

#### Functionality 4. Check for a Draw
- **Step**: Fill the grid with the following moves:  
  - Player X: top-left, center, bottom-right  
  - Player O: top-center, bottom-left, center-left, center-right, bottom-center  
- **Step**: The grid is now full with no player having three in a row.  
  **Expectation**: The game detects a draw and displays a message indicating that the game has ended in a draw.  

#### Functionality 5. Restart the Game
- **Step**: After a match ends (either win or draw), click the "Restart" button.  
  **Expectation**: The game resets the grid, and Player X is indicated to start again.  

#### Functionality 6. Timer Functionality
- **Step**: Start a new game.  
- **Step**: Observe the timer as players take turns.  
  **Expectation**: The timer counts up correctly, reflecting the duration of the match until the game ends.  

#### Functionality 7. Data Storage
- **Step**: Play a game and reach a conclusion (win or draw).  
- **Step**: Check the local text file where game results are stored.  
  **Expectation**: The file contains the correct result of the match, including the winner or draw status.  

#### Functionality 8. User Feedback at Game End
- **Step**: Complete a game with Player O winning.  
  **Expectation**: A message is displayed stating "Player O wins!" and provides an option to restart the game.  

#### Functionality 9. Invalid Move Handling
- **Step**: Player X attempts to place an "X" in a cell that is already occupied.  
  **Expectation**: The game prevents the move and displays an error message indicating that the cell is already taken.  