### Black Box Unit Test Cases  

#### Functionality 1. Input Total Amount of the Expense
- **Step**: Open the Expense Splitter application.  
- **Step**: Enter a valid total expense amount (e.g., $100) in the designated input field.  
  **Expectation**: The application accepts the input and displays the entered amount correctly.  

#### Functionality 2. Input Names of Individuals Involved in the Expense
- **Step**: Open the Expense Splitter application.  
- **Step**: Enter valid names (e.g., "Alice, Bob, Charlie") in the designated input field.  
  **Expectation**: The application accepts the input and displays the entered names correctly.  

#### Functionality 3. Calculate Share of Each Individual
- **Step**: Input a total expense amount of $100 and names "Alice, Bob, Charlie".  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application displays that each individual owes $33.33.  

- **Step**: Input a total expense amount of $200 and names "Alice, Bob".  
- **Step**: Click the "Calculate" button.  
  **Expectation**: The application displays that each individual owes $100.  

#### Functionality 4. Support Multiple Expenses to Manage and Split Over Time
- **Step**: Input a total expense amount of $100 and names "Alice, Bob".  
- **Step**: Click the "Calculate" button.  
- **Step**: Save the expense record.  
- **Step**: Input another total expense amount of $150 and names "Alice, Bob, Charlie".  
- **Step**: Click the "Calculate" button.  
- **Step**: Save the second expense record.  
  **Expectation**: The application retains both expense records and allows the user to view them in a list format.  

- **Step**: Open the saved expenses list.  
  **Expectation**: The list displays both expenses with their respective details, allowing the user to review past expenses.  