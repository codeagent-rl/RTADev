### Black Box Unit Test Cases  

#### Functionalities  1. User Registration
- **Step**: Register a new user with valid details (username, password, email).  
  **Expectation**: User is successfully registered, and a confirmation message is displayed.  


#### Functionalities  2. User Login
- **Step**: Log in with valid credentials (correct username and password).  
  **Expectation**: User is successfully logged in and redirected to the dashboard.  


#### Functionalities  3. View Dashboard
- **Step**: Log in successfully and access the dashboard.  
  **Expectation**: The dashboard displays navigation options, including book management, user management, and search books.  


#### Functionalities  4. Manage Books
- **Step**: Add a new book with valid details (title, author, isbn).  
  **Expectation**: The book is successfully added, and a confirmation message is displayed.  
-

#### Functionalities  5. Manage User Accounts
- **Step**: Add a new user with valid details (username, password, email).  
  **Expectation**: The user is successfully added, and a confirmation message is displayed.  
- **Step**: View the list of users after adding a new user.  
  **Expectation**: The newly added user appears in the user list.  


#### Functionalities  6. Search Books
- **Step**: Search for a book using a title that exists in the library.  
  **Expectation**: The search results display the book's details correctly.  


#### Functionalities  7. User Logout
- **Step**: Log out of the account successfully.  
  **Expectation**: The user is redirected to the login page and sees a logout confirmation message.  


#### Functionalities  8. File Handling for Data Storage
- **Step**: Add a new book and check the respective `.txt` file for the newly added entry.  
  **Expectation**: The book entry exists in the text file as expected.  
- **Step**: Delete a book and check the respective `.txt` file for the missing entry.  
  **Expectation**: The book entry is removed from the text file.  
