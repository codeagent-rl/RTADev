### Black Box Unit Test Cases  

#### Functionality 1. Input Receipt Information  
- **Step**: Open the Smart Receipt application.  
- **Step**: Enter the date as "2023-10-01", merchant as "Amazon", and total amount as "150.00".  
  **Expectation**: The receipt information is saved successfully, and a confirmation message is displayed.  

- **Step**: Enter the date as "2023-10-02", merchant as "Walmart", and total amount as "75.50".  
  **Expectation**: The receipt information is saved successfully, and a confirmation message is displayed.  

#### Functionality 2. Store and Organize Receipts  
- **Step**: Input multiple receipts with different dates and merchants.  
  **Expectation**: All receipts are stored in a local text file in an organized manner.  

#### Functionality 3. Search for Specific Receipts  
- **Step**: Input receipts with the following details:  
  - Date: "2023-10-01", Merchant: "Amazon", Amount: "150.00"  
  - Date: "2023-10-02", Merchant: "Walmart", Amount: "75.50"  
- **Step**: Use the search functionality to find receipts by entering "Amazon".  
  **Expectation**: The receipt from "Amazon" is displayed in the search results.  

#### Functionality 4. Retrieve Specific Receipts  
- **Step**: Input multiple receipts with different merchants and amounts.  
- **Step**: Search for a receipt using a total amount of "150.00".  
  **Expectation**: The receipt corresponding to the total amount of "150.00" is retrieved and displayed.  