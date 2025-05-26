### Black Box Unit Test Cases  

#### Functionality 1. User Registration
- **Step**: Navigate to the Registration Page.  
  **Expectation**: The Registration form is displayed.  


#### Functionality 2. User Login
- **Step**: Navigate to the Login Page.  
  **Expectation**: The Login form is displayed.  
 

#### Functionality 3. Add Items to Wishlist
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Expectation**: The Dashboard is displayed with an option to add items.  
 

#### Functionality 4. View Wishlist
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Expectation**: The wishlist is displayed, showing all added items with their details.  


#### Functionality 5. Update Item in Wishlist
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Step**: Select an item from the wishlist to update.  
  **Expectation**: The item details are displayed for editing.  
 

#### Functionality 6. Remove Item from Wishlist
- **Step**: Login successfully and navigate to the Dashboard Page.  
  **Step**: Select an item from the wishlist to remove.  
  **Expectation**: The item is removed from the wishlist, and a success message is displayed.  
 

#### Functionality 7. User Logout
- **Step**: Logout from the Dashboard Page.  
  **Expectation**: The user is redirected to the Login Page.  


#### Functionality 8. Data Persistence
- **Step**: Login successfully and add an item to the wishlist.  
  **Step**: Logout and close the application.  
  **Step**: Reopen the application and log back in.  
  **Expectation**: The previously added item is still present in the wishlist, demonstrating data persistence.  