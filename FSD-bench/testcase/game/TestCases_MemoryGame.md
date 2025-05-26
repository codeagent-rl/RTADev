### Black Box Unit Test Cases  

#### Functionality 1: Game Initialization and Card Setup
- **Step**: Start a new game.  
  **Expectation**: A grid of face-down cards is displayed, and the cards are shuffled randomly.  
- **Step**: Check the total number of cards displayed on the grid.  
  **Expectation**: The total number of cards should be twice the number of unique pairs (e.g., 16 cards for 8 pairs).  

#### Functionality 2: Flipping Cards
- **Step**: Click on the first card to flip it.  
  **Expectation**: The first card is revealed.  
- **Step**: Click on a second card to flip it.  
  **Expectation**: The second card is revealed.  
- **Step**: Click on two cards that do not match.  
  **Expectation**: After a brief delay, both cards are turned face-down again.  

#### Functionality 3: Matching Cards
- **Step**: Click on two cards that match.  
  **Expectation**: Both cards remain face-up.  
- **Step**: Continue flipping cards until all pairs are matched.  
  **Expectation**: All pairs are matched, and the board is cleared.  

#### Functionality 4: Timer Functionality
- **Step**: Start a new game and observe the timer.  
  **Expectation**: The timer starts counting from zero as soon as the game begins.  
- **Step**: Complete the game.  
  **Expectation**: The timer stops, and the final time is displayed.  

#### Functionality 5: Restarting the Game
- **Step**: Click the restart button during an ongoing game.  
  **Expectation**: The game resets, reshuffles the cards, and the timer resets to zero.  
- **Step**: Verify the state of the game after restarting.  
  **Expectation**: A new grid of face-down cards is displayed, and the timer is reset.  

#### Functionality 6: Scoring System
- **Step**: Complete a game and note the time taken.  
  **Expectation**: The score is calculated based on the time taken to finish the game.  
- **Step**: Complete another game faster than the previous one.  
  **Expectation**: The new score is higher than the previous score, reflecting the faster completion time.  

#### Functionality 7: Data Storage
- **Step**: Complete a game and check the local text file for scores.  
  **Expectation**: The score and time taken for the completed game are saved in the local text file.  
- **Step**: Restart the game and complete it again.  
  **Expectation**: The new score is appended to the local text file without overwriting the previous scores.  

#### Functionality 8: User Interface Responsiveness
- **Step**: Resize the game window during gameplay.  
  **Expectation**: The game interface adjusts appropriately without any distortion or loss of functionality.  
- **Step**: Attempt to click on cards while the game is in progress.  
  **Expectation**: The game responds to clicks only when it is in an active state (i.e., not during the delay after a mismatch).  