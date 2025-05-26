### Black Box Unit Test Cases  

#### Functionality 1. Control the Grid of Colored Blocks
- **Step**: Start the game and observe the initial grid of colored blocks.  
  **Expectation**: The grid is displayed with colored blocks arranged randomly.  
- **Step**: Select two adjacent blocks and attempt to swap them.  
  **Expectation**: The two blocks are swapped successfully if they are adjacent.

#### Functionality 2. Clear Blocks by Matching
- **Step**: Swap two blocks to create a match of three or more blocks of the same color.  
  **Expectation**: The matched blocks are cleared from the grid, and the remaining blocks fall into place.  
- **Step**: Create a match of four blocks of the same color.  
  **Expectation**: The blocks are cleared, and a special power-up is generated.

#### Functionality 3. Level Progression and Difficulty
- **Step**: Complete the first level by clearing the required number of blocks within the move limit.  
  **Expectation**: The game progresses to the next level, which features a larger grid and more complex arrangements.  
- **Step**: Attempt to start a level that exceeds the maximum allowed moves.  
  **Expectation**: The game prevents the player from starting the level and displays a message indicating the move limit.

#### Functionality 4. Scoring System
- **Step**: Clear a set of blocks and observe the score.  
  **Expectation**: The score increases based on the number of blocks cleared.  
- **Step**: Create a combo by clearing multiple matches in a single move.  
  **Expectation**: The score reflects the additional points earned from the combo.

#### Functionality 5. Power-ups Activation
- **Step**: Use a power-up to clear blocks in a specific pattern.  
  **Expectation**: The power-up activates and clears the designated blocks from the grid.  
- **Step**: Attempt to use a power-up when none are available.  
  **Expectation**: The game prevents the activation and displays a message indicating no power-ups are available.

#### Functionality 6. Move Limit Tracking
- **Step**: Start a level and track the number of moves used.  
  **Expectation**: The move counter accurately reflects the number of moves made.  
- **Step**: Exceed the move limit while attempting to complete a level.  
  **Expectation**: The game ends the level and displays a message indicating the player has exceeded the move limit.

#### Functionality 7. Bonus Points for Combos
- **Step**: Create a combo by clearing multiple matches in one move.  
  **Expectation**: The player receives bonus points added to their score.  
- **Step**: Clear blocks without creating a combo.  
  **Expectation**: The score increases, but no bonus points are awarded.

#### Functionality 8. Data Storage
- **Step**: Complete a level and check if the score is saved to a local text file.  
  **Expectation**: The score and level information are correctly written to the text file.  
- **Step**: Restart the game and check if the previously saved data is loaded correctly.  
  **Expectation**: The game loads the saved score and level data accurately.