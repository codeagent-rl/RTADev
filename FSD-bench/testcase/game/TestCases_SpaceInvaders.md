### Black Box Unit Test Cases  

#### Functionality 1. Player Controls Spaceship
- **Step**: Press the left arrow key to move the spaceship left.  
  **Expectation**: The spaceship moves left on the screen without leaving the game area.  
- **Step**: Press the right arrow key to move the spaceship right.  
  **Expectation**: The spaceship moves right on the screen without leaving the game area.  
- **Step**: Press the spacebar to shoot.  
  **Expectation**: A laser projectile is fired from the spaceship and moves upwards on the screen.  

#### Functionality 2. Destroying Alien Enemies
- **Step**: Position the spaceship directly below an alien enemy and press the spacebar to shoot.  
  **Expectation**: The alien enemy is destroyed, and a sound effect is played.  
- **Step**: Allow multiple aliens to descend and shoot at them.  
  **Expectation**: All hit aliens are destroyed, and the score increases accordingly.  

#### Functionality 3. Alien Movement
- **Step**: Start the game and observe the alien enemies.  
  **Expectation**: The aliens move horizontally across the screen and gradually descend lower with each movement.  
- **Step**: Allow the aliens to reach the bottom of the screen.  
  **Expectation**: The game ends if any alien reaches the bottom of the screen.  

#### Functionality 4. Avoiding Alien Projectiles
- **Step**: Start the game and allow aliens to shoot projectiles.  
  **Expectation**: The projectiles are visible and move downwards towards the player.  
- **Step**: Get hit by an alien projectile.  
  **Expectation**: The game ends, and a game over message is displayed.  

#### Functionality 5. Destroying Enemy Projectiles
- **Step**: Allow an alien to shoot a projectile towards the spaceship.  
  **Step**: Shoot the alien projectile with the spaceship's laser.  
  **Expectation**: The alien projectile is destroyed, and no damage is taken by the player.  
- **Step**: Move the spaceship to avoid an incoming alien projectile.  
  **Expectation**: The player successfully avoids the projectile, and the game continues.  

#### Functionality 6. Game End Conditions
- **Step**: Destroy all alien enemies on the screen.  
  **Expectation**: The game ends with a victory message displayed.  
- **Step**: Allow an alien projectile to hit the spaceship.  
  **Expectation**: The game ends with a game over message displayed.  