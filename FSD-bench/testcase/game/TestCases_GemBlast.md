### Black Box Unit Test Cases  

#### Functionality 1. Swap Gems
- **Step**: Select two adjacent gems to swap.  
  **Expectation**: The gems are swapped, and if a match of three or more gems of the same color is formed, those gems are highlighted for clearing.

#### Functionality 2. Clear Matches
- **Step**: Create a match of three or more gems of the same color.  
  **Expectation**: The matched gems are cleared from the grid, and new gems fall into the grid to replace them.  
- **Step**: Create a match of four gems of the same color.  
  **Expectation**: The matched gems are cleared, and the player earns bonus points for the larger match.

#### Functionality 3. Score Calculation
- **Step**: Create a match of three gems.  
  **Expectation**: The player earns a base score for the match.  
- **Step**: Create a match of five gems.  
  **Expectation**: The player earns a higher score for the larger match, reflecting the increased difficulty.

#### Functionality 4. Timer Limit
- **Step**: Start a new game and observe the timer.  
  **Expectation**: The timer starts counting down from the set limit.  
- **Step**: Allow the timer to reach zero without completing the level.  
  **Expectation**: The game ends, and the player is notified that the time is up.

#### Functionality 5. Combo and Chain Reactions
- **Step**: Create a move that results in multiple matches occurring simultaneously.  
  **Expectation**: The player earns bonus points for each match created in the combo.  
- **Step**: Create a move that causes a chain reaction of matches after the initial match is cleared.  
  **Expectation**: The player earns additional points for each match created by the chain reaction.

#### Functionality 6. Level Progression
- **Step**: Complete the current level successfully.  
  **Expectation**: The player is taken to the next level with increased difficulty.  
- **Step**: Attempt to start a new game after completing all levels.  
  **Expectation**: The player is given the option to replay previous levels or start a new game.

#### Functionality 7. Reset Game
- **Step**: Click the reset button during gameplay.  
  **Expectation**: The game resets to the initial state, clearing the grid and scores.  
- **Step**: Confirm the reset action.  
  **Expectation**: The game starts over, and the player can begin a new session.

#### Functionality 8. Grid Size and Complexity
- **Step**: Start a new game at a higher level.  
  **Expectation**: The grid size is larger, and the gem patterns are more complex than in previous levels.  
- **Step**: Observe the types of gems available in the higher level.  
  **Expectation**: New gem types are introduced, increasing the challenge of the game.

#### Functionality 9. Local Data Storage
- **Step**: Complete a game and check the local storage.  
  **Expectation**: The game results, including scores and levels completed, are saved in a local text file.  
- **Step**: Restart the game and check if previous scores are loaded correctly.  
  **Expectation**: The previously saved scores and game state are loaded accurately from the local storage.