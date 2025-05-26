import os
import re
import subprocess
import sys
import time
import signal

### reletive path: codebase
def read_codebase(codebase_path):
    content = []
    for root, _, files in os.walk(codebase_path):
        # Calculate the folder depth relative to the input codebase path
        depth = root[len(codebase_path):].count(os.sep)
        indent = "  " * depth

        for file in files:
            file_type = os.path.splitext(file)[-1].lower()
            if file_type in {".html", ".py"}:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    content.append(file_content + "\n\n")
                except Exception as e:
                    # Handle unreadable files
                    content.append(f"{indent}  --- FILE: {file} (ERROR: {e}) ---\n")
    return "".join(content)

def contains_placeholder(category, codebase: str) -> bool:
    # Define the list of placeholders to check
    placeholders = [
        r'\bPass\b',       # Matches "Pass" as a whole word
        r'\bTemp\b',       # Matches "Temp" as a whole word
        r'\bTBD\b',        # Matches "TBD" as a whole word
        r'\bTODO\b',       # Matches "TODO" as a whole word
        r'\bFIXME\b',      # Matches "FIXME" as a whole word
    ]
    placeholders_website = [
        r'\bPass\b',       # Matches "Pass" as a whole word
        r'\bTemp\b',       # Matches "Temp" as a whole word
        r'\bTBD\b',        # Matches "TBD" as a whole word
        r'\bTODO\b',       # Matches "TODO" as a whole word
        r'\bFIXME\b',      # Matches "FIXME" as a whole word
    ]
    # Combine placeholders into a single regex pattern
    if category == 'website':
        pattern = '|'.join(placeholders_website)
    else:
        pattern = '|'.join(placeholders)
    exception_handling_pattern = r"except\s+[^\n:]*:\s+pass"
    cleaned_codebase = re.sub(exception_handling_pattern, '', codebase, flags=re.MULTILINE)
    # Use re.search to check if the pattern exists in the codebase
    return bool(re.search(pattern, cleaned_codebase, re.IGNORECASE))

def clear_imports():
    for module in list(sys.modules.keys()):
        if module.startswith('testcode'):
            del sys.modules[module]

def check_software_via_command(program):
    try:
        process = subprocess.run(
                ["python", program],  # Replace "python" with the relevant interpreter/command
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5  # Set a timeout to avoid hanging
            )
        # Return True if execution succeeds
        return process.returncode == 0
    except Exception as e:
        print(f"Command execution failed: {e}")
        return False
    
def find_entry_file(codebase_path):
    entry_files = ["main.py", "app.py"]
    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file in entry_files:
                return file
    return None

def software_SC_Exec(category, codebase_path):
    codebase = read_codebase(codebase_path)
    sc = not contains_placeholder(category, codebase)
    # serch main.py or app.py path
    main_path = find_entry_file(codebase_path)
    os.chdir(codebase_path)
    print(f"CURRENT DIR {codebase_path}")
    clear_imports()
    # exe = check_software_via_command(main_path)
    return sc


project_categories = ['game', 'gui']

for project_category in project_categories:
    codebase_parent_path = f'/Users/liujie/Desktop/SD-bench/codebase-RTADev/{project_category}/'
    sc_cnt = 0
    exe_cnt = 0
    cnt = 0
    # 检查这个路径下的所有文件夹
    if os.path.isdir(codebase_parent_path):
        for project_name in os.listdir(codebase_parent_path):
            if project_name == '.DS_Store':
                continue
            print(f"----------------[START {project_name}]---------------------")
            project_path = os.path.join(codebase_parent_path, project_name)
            sc = software_SC_Exec(project_category, project_path)
            cnt += 1
            if sc:
                sc_cnt += 1
            else:
                print("contain placeholder" + project_path)
            
    print(f"{project_category}SC:{sc_cnt/cnt};")