import os
import openai
from openai import OpenAI
import re
import subprocess
import pandas as pd
import sys
import unittest
from prompt import prompt_for_game_testing, prompt_for_gui_testing, prompt_for_web_testing


### reletive path: codebase
def read_codebase(codebase_path):
    content = []
    for root, _, files in os.walk(codebase_path):
        # Calculate the folder depth relative to the input codebase path
        depth = root[len(codebase_path):].count(os.sep)
        indent = "  " * depth
        content.append(f"{indent}--- DIRECTORY: {root} ---\n")

        for file in files:
            file_type = os.path.splitext(file)[-1].lower()
            if file_type in {".html", ".py", ".txt", ".csv", ".json"}:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    annotation = f"{indent}  --- FILE: {file} (PATH: {file_path}, TYPE: {file_type}) ---\n"
                    content.append(annotation + file_content + "\n\n")
                except Exception as e:
                    # Handle unreadable files
                    content.append(f"{indent}  --- FILE: {file} (ERROR: {e}) ---\n")
    return "".join(content)

### reletive path: testcase
def read_md_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"Error: Could not read the file '{file_path}'. Reason: {e}"
    
### gpt api
def call_openai_api(prompt, model):
    # update the OpenAI client with your API key and base URL
    client = OpenAI(
    api_key="",
    base_url= ""
    )
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
    
def extract_python_code(llm_response):
    """
    Extract Python code blocks from LLM response.

    Args:
    - llm_response (str): The text response from LLM.

    Returns:
    - str: Extracted Python code.
    """
    # Use regex to extract code blocks between ```python and ```
    code_blocks = re.findall(r"```python\n(.*?)```", llm_response, re.DOTALL)
    return "\n\n".join(code_blocks)

def save_test_code(codebase_path, llm_response):
    """
    Extract Python code from LLM response and save it to testcode.py in the given codebase path.

    Args:
    - codebase_path (str): The path to the codebase folder where the file will be saved.
    - llm_response (str): The text response from LLM containing Python code.
    """
    # Ensure the path exists
    if not os.path.exists(codebase_path):
        os.makedirs(codebase_path)

    # Extract Python code from LLM response
    python_code = extract_python_code(llm_response)

    # Define the testcode.py file path
    testcode_path = os.path.join(codebase_path, "testcode.py")

    # Write the extracted code to testcode.py
    with open(testcode_path, "w", encoding="utf-8") as file:
        file.write(python_code)
    return testcode_path

def run_test_code(file_path):
    """
    Runs the Python script at the given file path and captures the output.

    Args:
    - file_path (str): Path to the Python file to run.

    Returns:
    - str: The output of the script execution.
    """
    try:
        result = subprocess.run(
            ["python", file_path], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error during execution: {e.stderr}"

def autogen():
    project_categories = ['gui','game']
    codebase_path = './codebase/'
    meta_data_path = "/Users/liujie/Desktop/SD-bench/RTADevSA_new60_result.csv"
    for project_category in project_categories:
        codebase_parent_path = f'./codebase/{project_category}/'
        # 检查这个路径下的所有文件夹
        if os.path.isdir(codebase_parent_path):
            for project_name in os.listdir(codebase_parent_path):
                project_path = os.path.join(codebase_parent_path, project_name)
                if os.path.exists(os.path.join(project_path, 'testcode.py')):
                    continue
                # 只处理文件夹
                if os.path.isdir(project_path):
                    print(f"Processing Project: {project_category}/{project_name}")
                    
                    results = read_results_from_csv(meta_data_path)
                # 检查项目是否已经在结果中
                    if project_name in results['project_name'].values:
                        print(f"Project {project_name} already exists in results, skipping...")
                        continue
                    # 确保代码库和测试用例路径正确
                    codebase_path = f'./codebase/{project_category}/{project_name}/'
                    testcase_path = f'./testcase/{project_category}/TestCases_{project_name}.md'

                    # 读取代码库和测试用例文件
                    codebase = read_codebase(codebase_path)
                    print(f"Codebase :\n{codebase}")
                    testcase = read_md_file(testcase_path)
                    print(f"Test Cases:\n{testcase}")

                    # 创建prompt并替换变量
                    prompt = None
                    if project_category == 'website':
                        prompt = prompt_for_web_testing
                    elif project_category == 'gui':
                        prompt = prompt_for_gui_testing
                    else:
                        prompt = prompt_for_game_testing
                    prompt = prompt.replace("{codebase}", codebase)
                    prompt = prompt.replace("{testcase}", testcase)

                    # 调用OpenAI API获取测试代码
                    test_code = call_openai_api(prompt=prompt, model='gpt-4o')
                    print(f"Test code:\n{test_code}")

                    # 保存生成的测试代码并运行测试
                    testcode_path = save_test_code(codebase_path=codebase_path, llm_response=test_code)
                    # run_test_code(testcode_path)
def write_results_to_csv(results, filename='test_results.csv'):
    # 使用 pandas 将结果写入 CSV 文件
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

def read_results_from_csv(filename='test_results.csv'):
    # 使用 pandas 从 CSV 文件读取数据
    df = pd.read_csv(filename)
    return df

def clear_imports():
    """
    Clears imported modules from sys.modules to avoid import errors
    when running tests in different directories.
    """
    for module in list(sys.modules.keys()):
        if module.startswith('testcode'):
            del sys.modules[module]
def runUnitTest():
    project_categories = ['gui','game']
    codebase_path = '/Users/liujie/Desktop/SD-bench/codebase'
    # category,project_name,passed,failed,errors,total
    meta_data_path = "/Users/liujie/Desktop/SD-bench/RTADevSA_new60_result.csv"

    for project_category in project_categories:
        codebase_parent_path = f'/Users/liujie/Desktop/SD-bench/codebase/{project_category}/'

        # 检查这个路径下的所有文件夹
        if os.path.isdir(codebase_parent_path):
            for project_name in os.listdir(codebase_parent_path):
                if project_name == '.DS_Store':
                    continue
                print(f"----------------[START {project_name}]---------------------")

                # 每次循环时重新加载结果
                results = read_results_from_csv(meta_data_path)

                # 检查项目是否已经在结果中
                if project_name in results['project_name'].values:
                    print(f"Project {project_name} already exists in results, skipping...")
                    continue

                project_path = os.path.join(codebase_parent_path, project_name)
                os.chdir(project_path)
                print(f"CURRENT DIR {project_path}")

                # 在加载测试前清理模块缓存
                clear_imports()

                # 加载测试文件 (testcode.py)
                loader = unittest.TestLoader()
                suite = unittest.TestSuite()

                # 自动加载 testcode.py 文件中的测试用例
                suite.addTests(loader.discover('.'))

                # 创建 TextTestRunner 实例，运行测试用例并输出结果
                runner = unittest.TextTestRunner()
                result = runner.run(suite)

                total = int(result.testsRun)
                passed = int(result.testsRun - len(result.failures) - len(result.errors))
                failed = len(result.failures)
                errors = len(result.errors)

                info = {
                    "category":project_category,
                    "project_name": project_name,
                    "passed": passed,
                    "failed": failed,
                    "errors": errors,
                    "total": total,
                }

                print(f"Total tests run: {total}")
                print(f"Passed: {passed}")
                print(f"Failed: {failed}")
                print(f"Errors: {errors}")
                print(f"----------------[END {project_name}]---------------------")

                new_row = pd.DataFrame([info])

                # 使用 pd.concat() 合并新的数据行
                results = pd.concat([results, new_row], ignore_index=True)

                # 写入 CSV 文件
                write_results_to_csv(results, meta_data_path)

                # 清除当前的测试套件和加载器
                suite._tests.clear()  # 清除测试套件中的测试用例
                loader = None  # 清除测试加载器对象
                suite = None  # 清空 TestSuite 对象

if __name__ == '__main__':
    autogen()
    # runUnitTest()
