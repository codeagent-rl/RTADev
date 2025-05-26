### Black Box Unit Test Cases  

#### Functionality 1. User Input for Weight and Height
- **Step**: Open the BMI Calculator application.  
- **Step**: Enter a valid weight (e.g., 70 kg) and height (e.g., 1.75 m).  
  **Expectation**: The application accepts the input without errors.  

#### Functionality 2. Calculate BMI
- **Step**: Input valid weight (e.g., 70 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application calculates and displays the BMI (e.g., 22.86).  

- **Step**: Input valid weight (e.g., 50 kg) and height (e.g., 1.60 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application calculates and displays the BMI (e.g., 19.53).  

#### Functionality 3. Classify BMI
- **Step**: Input valid weight (e.g., 70 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application classifies the BMI as "Normal" based on the calculated value.  

- **Step**: Input valid weight (e.g., 90 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application classifies the BMI as "Overweight" based on the calculated value.  

#### Functionality 4. View Interpretation of BMI
- **Step**: Input valid weight (e.g., 70 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application displays an interpretation message indicating a "Normal" BMI.  

- **Step**: Input valid weight (e.g., 50 kg) and height (e.g., 1.70 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application displays an interpretation message indicating "Underweight".  

#### Functionality 5. Provide BMI Recommendations
- **Step**: Input valid weight (e.g., 70 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application provides recommendations for maintaining a healthy lifestyle.  

- **Step**: Input valid weight (e.g., 95 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application provides recommendations for weight loss and healthy eating.  

#### Functionality 6. Data Storage
- **Step**: Input valid weight (e.g., 70 kg) and height (e.g., 1.75 m).  
- **Step**: Click the "Calculate" button.  
- **Step**: Save the results.  
  **Expectation**: The application saves the BMI result to a local text file successfully.  

- **Step**: Open the local text file after saving.  
  **Expectation**: The saved BMI result is correctly stored in the text file with the corresponding weight and height.  