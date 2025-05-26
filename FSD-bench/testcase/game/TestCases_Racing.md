### Black Box Unit Test Cases

#### Functionalities 1. Initialize the Game Interface  
- **Step**: Launch the game.  
  **Expectation**: The game interface loads successfully with three lanes displayed, all free of obstacles.  

#### Functionalities 2. Display Vehicle's Speed and Distance Traveled  
- **Step**: Start the game and move the vehicle forward.  
  **Expectation**: The speed and distance traveled are displayed correctly in the top right corner of the interface.  

#### Functionalities 3. Control Vehicle Speed  
- **Step**: Press the "up" arrow key.  
  **Expectation**: The vehicle's speed increases, and the current speed is reflected in the display.  

#### Functionalities 4. Control Vehicle's Lane Switching  
- **Step**: Press the "right" arrow key when the vehicle is in the left lane.  
  **Expectation**: The vehicle moves to the center lane without any obstacle collision.  

#### Functionalities 5. Simulate Obstacle Movement  
- **Step**: Run the game with obstacles defined in one of the lanes.  
  **Expectation**: The obstacles move backward while the vehicle remains stationary, simulating forward movement.  

#### Functionalities 6. Stop the Car  
- **Step**: Press the "s" key during the game.  
  **Expectation**: The vehicle's speed is set to 0, and it stops immediately.  

#### Functionalities 7. Handle Slow-Down Obstacle  
- **Step**: Move the vehicle to collide with a slow-down obstacle.  
  **Expectation**: The vehicle’s speed decreases as defined by the game’s mechanics.  

#### Functionalities 8. Handle Game-Ending Obstacle  
- **Step**: Move the vehicle to collide with a game-ending obstacle.  
  **Expectation**: The game ends immediately upon collision, presenting a game-over screen.  

#### Functionalities 9. Save Game Data to Local File  
- **Step**: Complete a lap and select the option to save the game progress.  
  **Expectation**: The game data is saved successfully to a local text file, reflecting the current state of the game.  