### Black Box Unit Test Cases  

#### Functionality 1. User Input for Conversion
- **Step**: Open the Unit Converter application.  
- **Step**: Input a valid numerical value (e.g., "10") in the input field.  
  **Expectation**: The application accepts the input value without errors.  

- **Step**: Input an invalid value (e.g., "abc") in the input field.  
  **Expectation**: The application displays an error message indicating invalid input.  

#### Functionality 2. Select Desired Unit for Conversion
- **Step**: Open the Unit Converter application.  
- **Step**: Select a unit from the dropdown menu (e.g., "Meters").  
  **Expectation**: The selected unit is displayed correctly in the interface.  

- **Step**: Change the selected unit to another unit (e.g., "Feet").  
  **Expectation**: The application updates the selected unit without errors.  

#### Functionality 3. Support for a Wide Range of Conversion Options
- **Step**: Open the Unit Converter application.  
- **Step**: Select "Length" from the conversion category.  
  **Expectation**: The application displays all available length units for conversion.  

- **Step**: Select "Weight" from the conversion category.  
  **Expectation**: The application displays all available weight units for conversion.  

#### Functionality 4. Support for Both Metric and Imperial Units
- **Step**: Open the Unit Converter application.  
- **Step**: Select "Temperature" and choose "Celsius" as the input unit.  
- **Step**: Select "Fahrenheit" as the output unit.  
  **Expectation**: The application allows conversion between metric (Celsius) and imperial (Fahrenheit) units.  

- **Step**: Select "Length" and choose "Miles" as the input unit.  
- **Step**: Select "Kilometers" as the output unit.  
  **Expectation**: The application allows conversion between imperial (Miles) and metric (Kilometers) units.  

#### Functionality 5. Display Converted Value with Precision
- **Step**: Open the Unit Converter application.  
- **Step**: Input a value (e.g., "1.5") and select "Kilometers" to "Miles".  
  **Expectation**: The application displays the converted value (e.g., "0.932") with appropriate precision.  

- **Step**: Input a value (e.g., "100") and select "Celsius" to "Fahrenheit".  
  **Expectation**: The application displays the converted value (e.g., "212.0") with appropriate precision.  