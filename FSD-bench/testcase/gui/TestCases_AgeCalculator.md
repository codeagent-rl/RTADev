### Black Box Unit Test Cases  

#### Functionality 1. User Input of Birthdate
- **Step**: Open the Age Calculator application.  
- **Step**: Enter a valid birthdate (e.g., "1990-05-15") in the input field.  
  **Expectation**: The application accepts the input without errors and displays a confirmation message indicating the birthdate has been recorded.  

#### Functionality 2. Calculate and Display Age
- **Step**: Input a valid birthdate (e.g., "1990-05-15").  
- **Step**: Click the "Calculate Age" button.  
  **Expectation**: The application displays the age as "33 years, 4 months, and 20 days" (assuming the current date is "2023-10-05").  

- **Step**: Input a birthdate that is today (e.g., "2023-10-05").  
- **Step**: Click the "Calculate Age" button.  
  **Expectation**: The application displays the age as "0 years, 0 months, and 0 days."  

#### Functionality 3. Calculate Days Until Next Birthday
- **Step**: Input a birthdate (e.g., "1990-05-15").  
- **Step**: Click the "Calculate Days Until Next Birthday" button.  
  **Expectation**: The application displays the number of days until the next birthday (e.g., "223 days" if the current date is "2023-10-05").  

- **Step**: Input a birthdate that is today (e.g., "2023-10-05").  
- **Step**: Click the "Calculate Days Until Next Birthday" button.  
  **Expectation**: The application displays "365 days" indicating the next birthday will be in one year.  