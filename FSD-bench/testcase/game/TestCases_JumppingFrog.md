### Black Box Unit Test Cases  

#### Functionality 1: Frog Movement Control
- **Step**: Press the left arrow key to move the frog left.  
  **Expectation**: The frog moves left on the screen.  
- **Step**: Press the right arrow key to move the frog right.  
  **Expectation**: The frog moves right on the screen.  
- **Step**: Press the 'A' key to move the frog left.  
  **Expectation**: The frog moves left on the screen.  
- **Step**: Press the 'D' key to move the frog right.  
  **Expectation**: The frog moves right on the screen.  

#### Functionality 2: Jumping Mechanism
- **Step**: Position the frog near a platform and press the spacebar to jump.  
  **Expectation**: The frog jumps forward and lands on the platform if within range.  
- **Step**: Position the frog at the edge of a platform and press the jump button.  
  **Expectation**: The frog jumps off the platform and falls into the water if no platform is below.  

#### Functionality 3: Platform Movement
- **Step**: Observe the platforms as they move horizontally.  
  **Expectation**: The platforms move smoothly across the screen.  
- **Step**: Position the frog on a moving platform and press the jump button.  
  **Expectation**: The frog jumps in the direction of the platform's movement and lands on another platform if timed correctly.  

#### Functionality 4: Game Over Condition
- **Step**: Allow the frog to fall into the water by missing all platforms.  
  **Expectation**: The game ends, and a game over message is displayed.  
- **Step**: After falling into the water, attempt to press the jump button.  
  **Expectation**: The game does not respond, and the player must restart the game.  

#### Functionality 5: Scoring System
- **Step**: Jump successfully onto a platform.  
  **Expectation**: The player's score increases by 1 point.  
- **Step**: Jump onto multiple platforms consecutively.  
  **Expectation**: The player's score reflects the total number of successful landings.  

#### Functionality 6: Timer Functionality
- **Step**: Start the game and begin jumping on platforms.  
  **Expectation**: A timer starts counting the duration of successful jumps.  
- **Step**: Observe the timer while jumping continuously.  
  **Expectation**: The timer updates in real-time, reflecting the total time the frog has been jumping without falling.  

#### Functionality 7: Data Storage
- **Step**: Complete a game session and achieve a score.  
  **Expectation**: The score is saved to a local text file.  
- **Step**: Restart the game and check the local text file.  
  **Expectation**: The previously saved score is present in the text file.  