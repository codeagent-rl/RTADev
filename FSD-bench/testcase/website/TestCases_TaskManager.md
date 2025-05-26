### Black Box Unit Test Cases  

#### Functionalities 1. User Login  
- **Step**: Enter a valid username and password.  
  **Expectation**: The user is logged in and navigated to the home page.  

#### Functionalities 2. User Registration  
- **Step**: Enter a new valid username, password, and email address.  
  **Expectation**: The account is created successfully, and the user is redirected to the login page with a success message.  

#### Functionalities 3. View Task List  
- **Step**: Successfully log in to the application.  
  **Expectation**: The user can view the task list on the home page.  


#### Functionalities 4. Add New Task  
- **Step**: Enter a valid task description and a due date.  
  **Expectation**: The task is correctly added to the task list, and a success message is displayed.  


#### Functionalities 5. Remove Task  
- **Step**: Click the "Remove Task" button next to a valid task.  
  **Expectation**: The task is removed from the task list, and a success message is displayed.  


#### Functionalities 6. Navigate Back to Login  
- **Step**: Click the "Back to Login" button on the home page.  
  **Expectation**: The user is navigated back to the login page.  


#### Functionalities 7. Task Data Storage  
- **Step**: Add a new task and check the local text file.  
  **Expectation**: The new task appears in the text file in the correct format.  
- **Step**: Remove a task and check the local text file.  
  **Expectation**: The removed task no longer appears in the text file.  


#### Functionalities 8. Invalid Actions  
- **Step**: Attempt to access the home page without logging in.  
  **Expectation**: The software redirects the user back to the login page with an error message.  


#### Functionalities 9. Session Management  
- **Step**: Log into the application and then close the browser without logging out.  
  **Expectation**: The session should not be valid when reopening the application, requiring login again.  

