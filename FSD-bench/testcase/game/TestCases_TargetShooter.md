### Black Box Unit Test Cases  

#### Functionality 1. Player Controls Shooter
- **Step**: Move the mouse to aim at a target on the screen.  
  **Expectation**: The shooter icon moves to align with the mouse cursor.  
- **Step**: Click the mouse button to shoot.  
  **Expectation**: A bullet is fired from the shooter towards the aimed direction.

#### Functionality 2. Moving Targets
- **Step**: Start a new game.  
  **Expectation**: Targets appear at random locations on the screen.  
- **Step**: Observe the targets for a duration of 10 seconds.  
  **Expectation**: Targets move around the screen continuously during this time.

#### Functionality 3. Shooting Accuracy and Speed
- **Step**: Shoot at a target and hit it.  
  **Expectation**: The score increases based on the accuracy of the shot.  
- **Step**: Shoot at multiple targets quickly within the time limit.  
  **Expectation**: The score reflects both the number of hits and the speed of shooting.

#### Functionality 4. Timer Countdown
- **Step**: Start a new game.  
  **Expectation**: A timer starts counting down from the set time limit (e.g., 60 seconds).  
- **Step**: Wait until the timer reaches zero.  
  **Expectation**: The game ends automatically when the timer runs out.

#### Functionality 5. Restart Game
- **Step**: Complete a round of the game.  
  **Step**: Click the "Restart" button.  
  **Expectation**: The game resets, and the player can start a new round.

#### Functionality 6. Increasing Difficulty Levels
- **Step**: Start the game at level 1.  
  **Expectation**: Targets appear at a certain speed and frequency.  
- **Step**: Progress to level 2 after completing level 1.  
  **Expectation**: Targets move faster and/or more targets appear on the screen.

#### Functionality 7. Leaderboard Tracking
- **Step**: Achieve a high score in a game round.  
  **Expectation**: The score is saved to the local leaderboard.  
- **Step**: View the leaderboard after completing multiple rounds.  
  **Expectation**: The leaderboard displays the highest scores in descending order.

#### Functionality 8. Competing for Top Spot
- **Step**: Play multiple rounds and achieve different scores.  
  **Expectation**: The scores are updated in the leaderboard accordingly.  
- **Step**: Achieve the highest score.  
  **Expectation**: The player's name is displayed at the top of the leaderboard.