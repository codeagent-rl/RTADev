### Black Box Unit Test Cases  

#### Functionalities 1. Connect Letters to Form a Word  
- **Step**: Player connects letters "C", "A", "T" to form a word.  
  **Expectation**: The word "CAT" is recognized as a valid word by the game.  

#### Functionalities 2. Scoring System  
- **Step**: Player forms the word "DOG" which is 3 letters long.  
  **Expectation**: The player receives 3 points for the word formed.  

#### Functionalities 3. Timer Functionality  
- **Step**: Start a new game and check the timer behavior.  
  **Expectation**: The timer should count down correctly from the set time limit without any interruptions.  

#### Functionalities 4. Difficulty Levels  
- **Step**: Select the "Hard" difficulty level for a new game.  
  **Expectation**: The game should set the appropriate rules for the hard level, such as fewer available letters or less time.  

#### Functionalities 5. Save Progress  
- **Step**: While in the middle of a game, invoke the save progress function.  
  **Expectation**: The current game state is successfully saved in a local text file.  

#### Functionalities 6. Load Saved Progress  
- **Step**: Load a previously saved game state from a text file.  
  **Expectation**: The game restores to the previous state accurately, including score and connected letters.  