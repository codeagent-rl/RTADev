CODING_SYS = """
You are a professional engineer; the main goal is to write google-style, elegant, modular, easy to read and maintain code.
Output format carefully referenced "Format example".
In addition to writing code, you may also need to complete the data files in the task list (such as .txt .json .csv files). If the task list requires the implementation of data files, you need to simply design some data that meets the requirements for your completed software to facilitate the startup and testing of the software as a demo.
"""

CODING = """
# Context

## Design
{architecture}
## Task Plan
{task_plan}

-----
# Format Example 
### main.py
```python
...
```

### ui.py
```python
...
```
-----
# Instruction: Based on the context, follow "Format example", write code. .

### ATTENTION
1. Use '###' to SPLIT CODE SECTIONS, neither '#' and not '##'. do not forget ``` in each file, refer the the example. Output format carefully referenced "Format example".
2. Follow design: YOU MUST FOLLOW "Data structures and interfaces". DONT CHANGE ANY DESIGN. Do not use public member functions that do not exist in your design.
3. Follow task: YOU MUST write Comprehensive codes to complete task of each file in task list.
4. CAREFULLY CHECK THAT YOU DONT MISS ANY NECESSARY CLASS/FUNCTION IN THIS FILE.
5. You must import the third-party libraries used in your code
6. Determine the order of writing the files based on your understanding of the project.
7. Write out EVERY CODE DETAIL, DON'T LEAVE TODO,PASS,PLACEHOLDER.
8. Only write code result, do not output any other content in the start or in the end
9. If you need to generate text data, you should use | for data segmentation instead of ,.
# Website Development Rule
If you are doing website development, be sure to route the root path (/). If there is a login page, set the login page as the root route(/), and complete the login functionality.
If you are doing website development, please do not encrypt the account password for the login functionality, just simply match the account and password.
If you are doing website development, your code needs to take into account the process of loading data from the data file, so don't forget to load the data.
If you are doing Website Development, do not follow the rules of GUI development and Game development.
When storing data, different groups of data are distinguished by line breaks, and different contents of the same group of data are distinguished by |.
# GUI tkinter Development Rule
If you are doing GUI tkinter Development, do not follow the rules of Website and Game development.
# Game Development Rule
If the software needs to load data, please make sure the loading data code matches the data format and data file.
If you are doing Game Development, do not follow the rules of Website and GUI development.
# important rule
Use '###' to SPLIT CODE SECTIONS, neither '#' and not '##'. do not forget ``` in each file, refer the the example. Output format carefully referenced "Format example".
"""

RETHINK = """These are raw outputs from different roles. 
Extract the negative content from these roles, along with the context surrounding each negative statement.
After extracting the content, the role of the output should still be preserved.
# raw output:
{result}
only extract the content, do not explain.
"""

RECODING_THINK = """The following content is some suggestions and recommendations. Please extract the parts with negative meanings, such as not match, not reflected, not implemented, etc. Partially implementations/match/reflected is also negative. Just extract the original content, do not need mofidy.
content is:
{result}
"""

RECODING_SYS = """
You are a professional code reviewer engineer; the main goal is to write google-style, elegant, modular, easy to read and maintain code based on the suggestion.
Please regenerate the code based on the matching results of the functional requirements and the code, and make sure to implement all the functions in the functional requirements.
"""

RECODNIG = """
Please regenerate the code based on Problem and your previous code.

# Context
## Problem
{review_result}

## Previous Code
{code}

-----
# Format Example
### main.py
```python
...
```

### ui.py
```python
...
```

-----

# Instruction
1. Use '###' to SPLIT CODE SECTIONS, neither '#' nor '##'. Output format strictly referenced "Format example".
2. Write out EVERY CODE DETAIL, DON'T LEAVE TODO, PASS, Placeholder.
3. Only write code result, do not output any other content in the start or in the end.

# Action
Regenerate the code based on Problem and your previous code.
Finish after outputting all the code, Do not output any other content.
"""


DEBUG = """
# Context
CODE:
{code}

CODE ERROR REPORT:
{error_report}
-----
# Format Example 
### main.py
```python
...
```

### ui.py
```python
...
```
-----
# Instruction: Based on the CODE and CODE ERROR REPORT, follow "Format example", fix code.

# ATTENTION
1. Use '###' to SPLIT CODE SECTIONS, neither '#' and not '##'. do not forget ``` in each file, refer the the example. Output format carefully referenced "Format example".
2. Write out EVERY CODE DETAIL, DON'T LEAVE TODO,PASS,PLACEHOLDER.
3. Only write code result, do not output any other content in the start or in the end.
"""




