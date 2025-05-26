### Black Box Unit Test Cases  

#### Functionality 1. Fill a 9x9 Grid with Symbols
- **Step**: Open the Sudoku Challenge game.  
- **Step**: Click on an empty cell in the grid and input a symbol (e.g., 'A').  
  **Expectation**: The symbol 'A' is displayed in the selected cell.  
- **Step**: Attempt to input a symbol in a cell that is already filled.  
  **Expectation**: The input is rejected, and the filled cell remains unchanged.  

#### Functionality 2. Ensure Unique Symbols in Rows, Columns, and Subgrids
- **Step**: Fill a row with symbols (e.g., 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I').  
- **Step**: Attempt to input a duplicate symbol (e.g., 'A') in the same row.  
  **Expectation**: The input is rejected, and an error message is displayed indicating the violation of Sudoku rules.  
- **Step**: Fill a column with symbols and then attempt to input a duplicate symbol in the same column.  
  **Expectation**: The input is rejected, and an error message is displayed.  

#### Functionality 3. Multiple Difficulty Levels
- **Step**: Start a new game and select 'Easy' difficulty.  
- **Expectation**: The game loads a puzzle with fewer initial symbols.  
- **Step**: Start a new game and select 'Hard' difficulty.  
- **Expectation**: The game loads a puzzle with more initial symbols and increased complexity.  

#### Functionality 4. Input Symbols Using Mouse Click or Keyboard
- **Step**: Click on an empty cell and type a symbol using the keyboard.  
  **Expectation**: The symbol appears in the selected cell.  
- **Step**: Click on an empty cell and then use the mouse to select a symbol from a palette.  
  **Expectation**: The selected symbol is placed in the clicked cell.  

#### Functionality 5. Track Time Taken to Solve Each Puzzle
- **Step**: Start a new game and solve the puzzle.  
- **Step**: Complete the puzzle.  
  **Expectation**: The time taken to solve the puzzle is displayed on the screen.  
- **Step**: Start another game and solve it faster than the previous one.  
  **Expectation**: The new time is displayed, and a message appears encouraging the player to beat their previous time.  

#### Functionality 6. Reset the Puzzle
- **Step**: Start a game and fill in several cells.  
- **Step**: Click the 'Reset' button.  
  **Expectation**: All filled cells are cleared, and the puzzle returns to its initial state.  
- **Step**: Click the 'New Puzzle' button after resetting.  
  **Expectation**: A new puzzle is loaded, allowing the player to choose the same or a different difficulty level.  