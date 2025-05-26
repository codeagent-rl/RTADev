### Black Box Unit Test Cases  

#### Functionalities 1. Connect Adjacent Blocks of the Same Color  
- **Step**: Drag a line between two adjacent blocks of the same color on the grid.  
  **Expectation**: The blocks are connected, and visual confirmation is provided that they will be cleared from the grid.  

#### Functionalities 2. Clear Connected Blocks from the Grid  
- **Step**: Successfully connect a group of adjacent blocks of the same color.  
  **Expectation**: The connected blocks are removed from the grid, and the grid updates correctly to reflect the changes.  

#### Functionalities 3. Validate Connection Based on Unobstructed Path  
- **Step**: Attempt to connect two blocks of the same color where the path is blocked by another block.  
  **Expectation**: The connection fails, and the user receives feedback indicating that the path is blocked.  

#### Functionalities 4. Track Player's Score  
- **Step**: Clear blocks from the grid after making a valid connection.  
  **Expectation**: The player's score increases appropriately based on the number of blocks cleared.  

#### Functionalities 5. Provide Visual Feedback on Successful Connections  
- **Step**: Connect two blocks of the same color.  
  **Expectation**: Visual feedback, such as an animation or highlight effect, occurs when the blocks are successfully connected and cleared.  

#### Functionalities 6. Start a New Game  
- **Step**: Select the option to start a new game from the menu.  
  **Expectation**: The game resets, initializing a new grid and player score while loading the first level.  

#### Functionalities 7. View High Scores  
- **Step**: Access the high scores from the menu.  
  **Expectation**: The high scores are displayed correctly, showing the top player scores from previous games stored in local text files.  

#### Functionalities 8. Increase Difficulty Across Levels  
- **Step**: Progress to the next level after completing the current one.  
  **Expectation**: The next level is loaded with a more complex grid setup or additional block colors compared to the previous level.  

#### Functionalities 9. Use Bonuses and Power-Ups  
- **Step**: Activate a bonus or power-up during gameplay.  
  **Expectation**: The bonus or power-up effect is applied, enhancing the gameplay experience (e.g., clearing adjacent blocks automatically).  