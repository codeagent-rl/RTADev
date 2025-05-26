### Black Box Unit Test Cases  

#### Functionality 1. User Registration
- **Step**: Navigate to the Registration Page.  
  **Expectation**: The Registration form is displayed with fields for username and password.  

#### Functionality 2. User Login
- **Step**: Navigate to the Login Page.  
  **Expectation**: The Login form is displayed with fields for username and password.  

#### Functionality 3. Equipment Management on Dashboard Page
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Expectation**: The equipment management interface is displayed.  

#### Functionality 4. View Equipment Details
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Expectation**: A list of available equipment is displayed.  

#### Functionality 5. Set Alerts for Equipment Maintenance
- **Step**: Navigate to the Dashboard Page and select an equipment item.  
  **Step**: Set a maintenance alert for the equipment.  
  **Expectation**: The alert is saved, and a confirmation message is displayed.  

#### Functionality 6. Search for Equipment
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Step**: Enter a specific equipment name in the search bar.  
  **Expectation**: The equipment list is filtered to show only the matching items.  


#### Functionality 7. Filter Equipment List
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Step**: Apply a filter based on equipment condition (e.g., "Good").  
  **Expectation**: The equipment list updates to show only items that match the selected condition.  


#### Functionality 8. User Logout
- **Step**: Logout from the Dashboard Page.  
  **Expectation**: The user is redirected to the Login Page.  


#### Functionality 9. Data Persistence
- **Step**: Login successfully and add a new equipment item.  
  **Step**: Logout and close the application.  
  **Step**: Reopen the application and log in again.  
  **Expectation**: The previously added equipment item is still present in the inventory list.