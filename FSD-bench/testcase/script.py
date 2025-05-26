import os
import re

def count_expectation_in_file(file_path):
    """
    统计单个 .md 文件中 "Expectation" 的出现次数
    """
    count = 0
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                count += len(re.findall(r'\bExpectation\b', line))  # 仅匹配完整单词
    except Exception as e:
        print(f"无法读取文件 {file_path}: {e}")
    return count

def process_directory(base_path):
    """
    遍历 website、game、gui 目录，统计所有 .md 文件中 "Expectation" 的总出现次数
    """
    categories = ["website", "game", "gui"]
    total_expectation_count = 0
    file_count = 0

    for category in categories:
        category_path = os.path.join(base_path, category)
        if os.path.exists(category_path) and os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith(".md"):
                    file_path = os.path.join(category_path, file)
                    count = count_expectation_in_file(file_path)
                    total_expectation_count += count
                    file_count += 1
                    print(f"{file}: {count} 次")

    return file_count, total_expectation_count

def main():
    base_path = os.getcwd()  # 当前目录
    file_count, total_expectation = process_directory(base_path)

    print("\n统计结果:")
    print(f"总 .md 文件个数: {file_count}")
    print(f'"Expectation" 总出现次数: {total_expectation}')

if __name__ == "__main__":
    main()