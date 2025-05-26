### Black Box Unit Test Cases  

#### Functionality 1. Input Desired Time Duration
- **Step**: Open the QuickTimer application.  
- **Step**: Input a valid time duration (e.g., "5 minutes") in the designated input field.  
  **Expectation**: The application accepts the input and displays it correctly in the input field.  

#### Functionality 2. Start Timer with a Single Click
- **Step**: Input a valid time duration (e.g., "10 seconds") in the input field.  
- **Step**: Click the "Start Timer" button.  
  **Expectation**: The timer starts counting down from the specified duration, and the button changes to "Stop Timer".  

- **Step**: Input a valid time duration (e.g., "15 seconds") in the input field.  
- **Step**: Click the "Start Timer" button, then click it again to stop the timer.  
  **Expectation**: The timer stops, and the countdown is paused.  

#### Functionality 3. Notifications When Timer Reaches Zero
- **Step**: Input a short time duration (e.g., "5 seconds") in the input field.  
- **Step**: Click the "Start Timer" button.  
  **Expectation**: After 5 seconds, a notification alert appears indicating that the timer has reached zero.  