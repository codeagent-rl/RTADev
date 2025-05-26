### Black Box Unit Test Cases  

#### Functionalities 1. Select and Connect Blocks of the Same Color  
- **Step**: Select two or more blocks of the same color on the grid.  
  **Expectation**: The selected blocks are connected and cleared from the board.

#### Functionalities 2. Display the Game Grid  
- **Step**: Launch the game application.  
  **Expectation**: The game grid appears, displaying blocks of various colors.

#### Functionalities 3. Score Calculation After Block Clearing  
- **Step**: Connect and clear three blocks of the same color.  
  **Expectation**: The score increases by three points, reflecting the number of blocks cleared.

#### Functionalities 4. Blocks Fall to Occupy Spaces  
- **Step**: Clear blocks from the middle of the grid.  
  **Expectation**: The blocks above the cleared spaces fall down to fill the gaps, and new blocks appear.

#### Functionalities 5. Undo Last Move  
- **Step**: Connect blocks and then use the undo function.  
  **Expectation**: The previous connection is reverted, and the blocks return to their initial positions.

#### Functionalities 6. Save Game State to a Local File  
- **Step**: Save the game progress using the save function.  
  **Expectation**: The game state is saved successfully to a local text file without errors.

#### Functionalities 7. Load Game State from a Local File  
- **Step**: Load a saved game state from a local text file.  
  **Expectation**: The game state is restored correctly, with blocks and score reflecting the saved state.