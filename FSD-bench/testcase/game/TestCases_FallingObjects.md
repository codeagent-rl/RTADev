### Black Box Unit Test Cases  

#### Functionality 1. Player Controls the Basket
- **Step**: Launch the game and observe the initial position of the basket.  
  **Expectation**: The basket is displayed at the bottom center of the screen.  
- **Step**: Press the left arrow key.  
  **Expectation**: The basket moves left on the screen.  
- **Step**: Press the right arrow key.  
  **Expectation**: The basket moves right on the screen.  
- **Step**: Hold the left arrow key down.  
  **Expectation**: The basket continues to move left until the key is released, without moving off the screen.  
- **Step**: Hold the right arrow key down.  
  **Expectation**: The basket continues to move right until the key is released, without moving off the screen.  

#### Functionality 2. Catching Falling Objects
- **Step**: Start the game and allow an object to fall.  
  **Step**: Move the basket to catch the falling object.  
  **Expectation**: The score increases by 1 when the object is caught.  
- **Step**: Allow an object to fall without catching it.  
  **Expectation**: The number of missed objects increases by 1 when the object hits the ground.  

#### Functionality 3. Scoring System
- **Step**: Catch multiple falling objects in succession.  
  **Expectation**: The score reflects the total number of objects caught.  
- **Step**: Miss a certain number of objects (e.g., 3).  
  **Expectation**: The game ends, and a message is displayed indicating the player has lost.  

#### Functionality 4. Game End Conditions
- **Step**: Start the game and set a timer for a specific duration (e.g., 60 seconds).  
- **Step**: Play the game until the timer runs out.  
  **Expectation**: The game ends when the timer reaches zero, and the final score is displayed.  
- **Step**: Miss the maximum allowed number of objects (e.g., 3).  
  **Expectation**: The game ends immediately, and a message is displayed indicating the player has lost.  

#### Functionality 5. Data Storage
- **Step**: Play the game and achieve a score.  
- **Step**: End the game and check the local text file for saved data.  
  **Expectation**: The score is correctly saved in the local text file.  
- **Step**: Restart the game after saving the score.  
  **Expectation**: The previously saved score is loaded correctly from the local text file.  