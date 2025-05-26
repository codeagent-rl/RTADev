### Black Box Unit Test Cases  

#### Functionalities 1. Initialize the Game Board  
- **Step**: Start a new Gomoku game.  
  **Expectation**: The game board is initialized with the correct grid size and is displayed properly.  

#### Functionalities 2. Assign Player Colors  
- **Step**: Begin the game and assign colors to two players.  
  **Expectation**: Player one receives black pieces and player two receives white pieces.  

#### Functionalities 3. Place a Piece on the Board  
- **Step**: Player one clicks on an empty square to place a piece.  
  **Expectation**: The specified square is marked with a black piece, and the move is registered.  

#### Functionalities 4. Check for Victory  
- **Step**: After placing pieces, check if a player has won.  
  **Expectation**: If a player aligns five pieces consecutively, the game announces the winner and prevents further moves.  

#### Functionalities 5. Display Winning Player Information  
- **Step**: Trigger the victory condition.  
  **Expectation**: The winning player's name and color are displayed prominently on the board.  

#### Functionalities 6. Prevent Further Moves After Victory  
- **Step**: Attempt to place a piece after a victory has been declared.  
  **Expectation**: The game does not allow any further piece placements and provides a message indicating that the game has ended.  

#### Functionalities 7. Save Game State to a File  
- **Step**: Save the current game state to a local text file.  
  **Expectation**: The game state is stored successfully in the file, reflecting the current board and player turns.  

#### Functionalities 8. Load Game State from a File  
- **Step**: Load a previously saved game state from a text file.  
  **Expectation**: The game board accurately reflects the state saved in the file, with all pieces in their correct positions.  

#### Functionalities 9. Validate Input for Piece Placement  
- **Step**: Attempt to place a piece in a non-empty or out-of-bounds square.  
  **Expectation**: The action is rejected and an error message is displayed, indicating that the move is invalid.  

