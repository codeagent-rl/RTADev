### Black Box Unit Test Cases  

#### Functionality 1. Enable Text File Creation and Editing
- **Step**: Open Notepad Plus application.  
  **Expectation**: The application launches successfully, displaying a blank text area for editing.  
- **Step**: Type "Hello, World!" in the text area.  
  **Expectation**: The text "Hello, World!" appears in the text area.  
- **Step**: Save the file with the name "test.txt".  
  **Expectation**: The file is saved successfully in the local storage, and a confirmation message is displayed.  
- **Step**: Open "test.txt" in Notepad Plus.  
  **Expectation**: The text "Hello, World!" is displayed in the text area.

#### Functionality 2. Provide Syntax Highlighting for Various Programming Languages
- **Step**: Open a new text file in Notepad Plus.  
- **Step**: Set the language mode to Python.  
- **Step**: Type the following code:  
  ```python
  def hello():
      print("Hello, World!")
  ```
  **Expectation**: The keywords "def" and "print" are highlighted according to Python syntax rules.  
- **Step**: Change the language mode to JavaScript.  
- **Step**: Type the following code:  
  ```javascript
  function hello() {
      console.log("Hello, World!");
  }
  ```
  **Expectation**: The keywords "function" and "console.log" are highlighted according to JavaScript syntax rules.

#### Functionality 3. Offer Code Indentation Features
- **Step**: Open a new text file in Notepad Plus.  
- **Step**: Type the following code without indentation:  
  ```python
  def hello():
  print("Hello, World!")
  ```
- **Step**: Select the line with `print("Hello, World!")` and apply indentation.  
  **Expectation**: The line is indented correctly under the function definition.  
- **Step**: Use the "Unindent" feature on the indented line.  
  **Expectation**: The line returns to its original position without indentation.

#### Functionality 4. Provide Search Functionality
- **Step**: Open a text file containing the text "Hello, World!".  
- **Step**: Use the search feature to find "World".  
  **Expectation**: The search highlights the word "World" in the text area.  
- **Step**: Click "Next" to find the next occurrence.  
  **Expectation**: If there are no more occurrences, a message indicates that the search has reached the end of the document.

#### Functionality 5. Provide Replace Functionality
- **Step**: Open a text file containing the text "Hello, World!".  
- **Step**: Use the replace feature to replace "World" with "Universe".  
  **Expectation**: The text changes to "Hello, Universe!" in the text area.  
- **Step**: Use the replace feature to replace "Hello" with "Greetings".  
  **Expectation**: The text changes to "Greetings, Universe!" in the text area.

#### Functionality 6. Offer Customizable Themes
- **Step**: Open Notepad Plus application.  
- **Step**: Navigate to the settings menu to change the theme.  