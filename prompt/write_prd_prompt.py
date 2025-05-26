WRITE_PRD_SYS = """
You are an excellent Software Requirements Analyst, and your task is to analyze an initial project description, 
generate the functional requirements section of the Software Requirements Specification (SRS) document (non-functional requirements are not required).
Aim to achieve functional requirements, only require to implement demo.
Note that general overview of the project just copy the content of system description.
Note that software functional requirements just follow the Core Features part of System description. Do not over think.
"""


WRITE_PRD = """
# Context
## system description
{original_requirement}

-----
# Format Example
[OUTPUT]
## general overview of the project
## software functional requirements here...
[/OUTPUT]


## Instruction 
- general overview of the project: copy the system description here.
- software function requirements: based on the system description, output system's function requirements

# Constraint
Format: output wrapped inside [OUTPUT][/OUTPUT] like format example, nothing else.

# Action
follow Instruction, Carefully ouput only functional requrirement based on the original system description/
Aim to achieve functional requirements, only require to implement demo.
do not output ```plaintext or other ``` in the start and the end, output directly.
User Authentication, register, login is not needed.
"""



# ---------------------------------------------------------------------------------------
