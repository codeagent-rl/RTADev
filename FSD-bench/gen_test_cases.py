import sys
import os
from openai import OpenAI
from gen_test_cases_prompt import prompt_for_gen_test_cases
### gpt api
def call_openai_api(prompt, model):
    # Initialize OpenAI client with your API key and base URL
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
    

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_test_cases():
    """生成测试用例"""
    dataset_path = 'dataset/SD-bench/dataset'
    test_cases_path = 'dataset/SD-bench/testcase'
    categories = ['website', 'game', 'gui']
    for category in categories:
        data_path = f'{dataset_path}/{category}'
        for file in os.listdir(data_path):
            if file.endswith('.md'):
                md_file_path = f'{data_path}/{file}'
                software_description = read_file(md_file_path)
                test_cases = f'{test_cases_path}/{category}/TestCases_{file[:-3]}.md'
                if os.path.exists(test_cases):
                    continue
                prompt = prompt_for_gen_test_cases.format(software_description=software_description)
                response = call_openai_api(prompt, model="gpt-4o-mini")
                print(f'-----[Processing]: {category}-----')
                print(response)
                write_file(test_cases, response)
        
if __name__ == '__main__':
    generate_test_cases()
            