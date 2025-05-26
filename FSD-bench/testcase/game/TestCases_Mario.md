### Black Box Unit Test Cases  

#### Functionalities 1. Move Mario
- **Step**: Press the right arrow key to move Mario right.  
  **Expectation**: Mario's position on the screen updates to the right by one unit.

#### Functionalities 2. Jump with Mario
- **Step**: Press the up arrow key to make Mario jump.  
  **Expectation**: Mario moves upward and then falls back down, simulating a jump.

#### Functionalities 3. Interact with a Block
- **Step**: Position Mario below a block and press the down arrow key to hit the block.  
  **Expectation**: A mushroom appears above the block, and the score increases by 100.

#### Functionalities 4. Collect a Mushroom
- **Step**: Move Mario to touch a mushroom.  
  **Expectation**: The mushroom disappears, and the score increases by 1000.

#### Functionalities 5. Encounter an Enemy
- **Step**: Move Mario into the path of an enemy.  
  **Expectation**: Mario loses a life, and the game emits a 'lose' sound.

#### Functionalities 6. Reach the Flagpole
- **Step**: Move Mario to the flagpole and touch it.  
  **Expectation**: The game ends, and the score increases by 10000.

#### Functionalities 7. Score Increases Over Time
- **Step**: Wait for one second during gameplay.  
  **Expectation**: The score increases by 1.

#### Functionalities 8. Follow Mushroom Behavior
- **Step**: Allow the mushroom to fall after being released from the block.  
  **Expectation**: The mushroom moves left and falls to the ground correctly.

#### Functionalities 9. Enemy Movement Behavior
- **Step**: Observe the enemy's movement pattern over several seconds.  
  **Expectation**: The enemy moves left and right randomly within its boundaries. 

#### Functionalities 10. Save Game Data
- **Step**: End the game and attempt to save the game data (score and state) to a text file.  
  **Expectation**: The game data is saved successfully in the specified text file format. 