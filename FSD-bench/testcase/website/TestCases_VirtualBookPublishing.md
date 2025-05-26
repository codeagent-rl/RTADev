### Black Box Unit Test Cases  

#### Functionalities  1. User Login  
- **Step**: Enter a valid username and password.  
  **Expectation**: The user is logged in successfully and redirected to the Dashboard Page.  

#### Functionalities  2. Navigation to Registration Page  
- **Step**: Click the Registration link on the Login Page.  
  **Expectation**: The software navigates to the Registration Page.  

#### Functionalities  3. User Registration  
- **Step**: Enter a valid username and password and submit the form.  
  **Expectation**: The user is registered successfully and redirected to the Login Page with a welcome message.  

#### Functionalities  4. Accessing the Dashboard Page  
- **Step**: Log in successfully.  
  **Expectation**: The Dashboard Page is displayed with a welcome message and navigation options.  

#### Functionalities  5. Create New Book  
- **Step**: Navigate to Create New Book Page from the Dashboard.  
  **Expectation**: The Create New Book Page is displayed with fields for title, author, and content.  
- **Step**: Enter valid title, author, and content and submit the form.  
  **Expectation**: The book details are saved successfully, and the user is redirected to the My Books Page.  


#### Functionalities  6. View My Books  
- **Step**: Navigate to My Books Page from the Dashboard.  
  **Expectation**: The My Books Page is displayed with a list of published books.  

#### Functionalities  7. View Book Details  
- **Step**: Click the View button next to a book on the My Books Page.  
  **Expectation**: The Book Details Page is displayed with the title, author, and content of the selected book.  

#### Functionalities  8. Navigate Back to My Books Page  
- **Step**: View details of a book on the Book Details Page.  
  **Expectation**: An option to navigate back to the My Books Page is available.  
- **Step**: Click the back navigation link.  
  **Expectation**: The user is redirected back to the My Books Page with the previously viewed books listed.  

#### Functionalities  9. View About Page  
- **Step**: Navigate to the About Page from the Dashboard.  
  **Expectation**: The About Page is displayed with information about the application, its version, and support contact details.  


#### Functionalities  10. Data Storage using Text Files  
- **Step**: Create a new book and check the local text file storage.  
  **Expectation**: The book details are saved correctly in the designated text file format.  
- **Step**: Delete the text file where books are stored.  
  **Expectation**: The software displays an error message on attempting to view or create books, indicating data storage could not be accessed.  