### Black Box Unit Test Cases  

#### Functionality 1. Set a timer for work intervals and breaks
- **Step**: Open the FocusTime application.  

- **Step**: Set the work interval timer to 25 minutes and the break timer to 5 minutes.  
  **Expectation**: The timers are set correctly, displaying 25:00 for work and 05:00 for breaks.  

  

#### Functionality 2. Customize the duration of work intervals and breaks
- **Step**: Open the FocusTime application.  
- **Step**: Change the work interval to 30 minutes and the break to 10 minutes.  
  **Expectation**: The application saves the new settings, and the timers display 30:00 for work and 10:00 for breaks.  

- **Step**: Start the break timer after completing the work interval.  
  **Expectation**: The break timer counts down from 10:00 to 00:00, indicating the break session is in progress. 

#### Functionality 3. Provide notifications and reminders for work sessions
- **Step**: Set a work interval of 1 minute for testing purposes.  
- **Step**: Start the work interval timer.  
  **Expectation**: A notification appears when the timer reaches 00:00, indicating the end of the work session.  

- **Step**: Set a reminder for a break after 1 minute of work.  
- **Step**: Wait for the timer to reach 00:00.  
  **Expectation**: A reminder notification appears after the work session ends, prompting the user to take a break.  