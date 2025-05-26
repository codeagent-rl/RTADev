### Black Box Unit Test Cases  

#### Functionality 1. Find Hidden Words in the Grid
- **Step**: Start a new game with a predefined grid containing the word "CAT".  
  **Expectation**: The player can successfully connect the letters C, A, and T in the grid to form the word "CAT", and the score is updated accordingly.  
- **Step**: Attempt to connect letters that do not form a valid word (e.g., C, A, G).  
  **Expectation**: The game does not recognize the connection as a valid word, and the score remains unchanged.  

#### Functionality 2. Score Calculation
- **Step**: Complete a game by finding all the hidden words in the grid.  
  **Expectation**: The final score reflects the total points for all words found, and a summary of the words is displayed.  
- **Step**: Find a word that has a higher point value (e.g., a longer word) and check the score.  
  **Expectation**: The score increases appropriately based on the point value assigned to the word found.  

#### Functionality 3. Level Progression
- **Step**: Complete the first level of the game.  
  **Expectation**: The player is automatically advanced to the next level with a larger grid and a new set of words.  
- **Step**: Attempt to start a new game at a higher difficulty level without completing the previous levels.  
  **Expectation**: The game prompts the player to complete the previous levels before advancing to a higher difficulty.  

#### Functionality 4. Timer Functionality
- **Step**: Start a new game and observe the timer.  
  **Expectation**: The timer begins counting down as soon as the game starts.  
- **Step**: Complete the game and check the final time displayed.  
  **Expectation**: The final time reflects the total duration taken to find all the words, and it is displayed in a readable format.  

#### Functionality 5. Data Storage
- **Step**: Save the game progress after completing a level.  
  **Expectation**: The game state is correctly saved in a local text file, and the player can resume from that point later.  
- **Step**: Load a previously saved game.  
  **Expectation**: The game resumes from the saved state, with the grid and score reflecting the last saved progress.  