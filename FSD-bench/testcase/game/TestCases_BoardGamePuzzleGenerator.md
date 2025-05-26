### Black Box Unit Test Cases  

#### Functionalities 1. Select Puzzle Category  
- **Step**: User selects "logic puzzles" from the available categories.  
  **Expectation**: The application confirms the selection and prepares to generate a puzzle from the "logic puzzles" category.  

#### Functionalities 2. Generate a New Puzzle  
- **Step**: Start a new game after selecting a category.  
  **Expectation**: A unique puzzle is generated and displayed on the screen corresponding to the selected category.  

#### Functionalities 3. Start the Timer  
- **Step**: Start the game with a new puzzle.  
  **Expectation**: The timer starts counting up, indicating the elapsed time since the puzzle was generated.  

#### Functionalities 4. Calculate Player’s Score  
- **Step**: Player solves the puzzle in under 5 minutes with no incorrect attempts.  
  **Expectation**: The scoring system generates a score based on the time and accuracy of the solution, reflecting the player's performance.  

#### Functionalities 5. Submit Solution  
- **Step**: Player submits a solution for the generated puzzle.  
  **Expectation**: The application provides immediate feedback indicating whether the submitted solution is correct or incorrect.  

#### Functionalities 6. View Puzzle Feedback  
- **Step**: Player submits a solution and awaits feedback.  
  **Expectation**: Feedback is displayed on the screen, indicating the correctness of the solution along with any hints or explanations if incorrect.  

#### Functionalities 7. Timer Stops on Solution Submission  
- **Step**: Player submits an answer for the puzzle.  
  **Expectation**: The timer stops, and the final time taken to solve the puzzle is recorded and displayed to the player.  

#### Functionalities 8. Load Puzzle Data from File  
- **Step**: Application attempts to load puzzle information from a local text file.  
  **Expectation**: The puzzle data is successfully loaded or an error message is displayed if the file is not found.  

#### Functionalities 9. Validate Puzzle Solution Format  
- **Step**: Player submits a solution in an incorrect format (e.g., string instead of a number).  
  **Expectation**: The application flags the submission as invalid and prompts the player to input the solution in the correct format.  