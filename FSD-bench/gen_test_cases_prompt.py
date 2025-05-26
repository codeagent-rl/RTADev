prompt_for_gen_test_cases = """
{software_description}

# Instruction
Based on the software description given above, write test cases(1 or 2 test cases) for each of the core features. 
In this case, multiple test cases for the same feature should be written together.

----------------------------------
# Example Output
### Black Box Unit Test Cases  

#### Funtionality  1. User Login 
- **Step**: Navigate to Login Page.
- **Step**: Enter a valid username and password.  
  **Expectation**: Access is granted, and the user is redirected to the Dashboard Page.  

#### Funtionality  2. Navigate to Registration Page and User Registration
- **Step**: Click on the "Register here" link on the Login Page.  
  **Expectation**: The user is redirected to the Registration Page.  
- **Step**: Fill in valid username and password on the Registration Page.  
  **Expectation**: The user is registered successfully, and a confirmation message is displayed.  

#### Funtionality  3. View Charities on the Dashboard Page 
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Expectation**: A list of available charities is displayed.  
- **Step**: Refresh the Dashboard Page after adding a new charity in the local storage.  
  **Expectation**: The newly added charity appears in the charity list.  

#### Funtionality  4. Navigate to Charity Details Page 
- **Step**: Click the 'Details' button for a specific charity on the Dashboard Page.  
  **Expectation**: The Charity Details Page for that charity is displayed, showing detailed information.  

#### Funtionality  5. View Contribution History 
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Expectation**: The user's contribution history is displayed correctly.  

#### Funtionality  6. Donate to a Charity 
- **Step**: Navigate to the Charity Details Page for a specific charity.  
  **Step**: Enter a valid donation amount and click the donate button.  
  **Expectation**: The donation is processed successfully, and a confirmation message is displayed.   

#### Funtionality  7. User Logout 
- **Step**: Logout from the Dashboard Page.  
  **Expectation**: The user is redirected to the Login Page.  

#### Funtionality  8. Navigate Back to Dashboard 
- **Step**: Navigate to the Charity Details Page.  
  **Step**: Click the back button to return to the Dashboard Page.  
  **Expectation**: The user is redirected back to the Dashboard Page with the charity list shown.  

#### Funtionality  9. View Detailed Information
- **Step**: Click the 'Details' button for a specific charity on the Dashboard Page.  
- **Step**: Select a specific charity by clicking on a charity's 'Details' buttion.
  **Expectation**: The specific charity's details for that charity is displayed, showing detailed information.  

"""