import dashscope
from datetime import datetime
import argparse

from utils.commen import read_yaml
from agents.team import Team


# the __init__ of the agents folder has already imported the class, there's no need to write additional class import statements.
from agents import *
from model.model import Qwen, GPT

from langchain_openai import ChatOpenAI

import json
import os
import re
import argparse
def start_project():
    parser = argparse.ArgumentParser(description="original Requirement")
    parser.add_argument("--category", type=str, help="gui")
    parser.add_argument("--name", type=str, help="DailyHealthTips.md")
    args = parser.parse_args()
    print(f"Received Original Requirement Name : {args.name}")
    ### dataset path
    category = args.category
    name = args.name
    project_description_path = f'/Users/liujie/Desktop/SD-bench/dataset/{category}/{name}'
    # framework execution start time
    start_time = datetime.now()
    
    
    match = re.match(r"^(.*)\.md$", name)
    if match:
        project_name = match.group(1)
        print(project_name)
    ### 读取project_description_path中的md文件内容至project_description
    with open(project_description_path, "r", encoding="utf-8") as file:
        project_description = file.read()
    origin_req = project_description
    # Build Agent's Team
    team = Team()
    Team.project_name = project_name
    projdir = (
        "./project/"
        + category
        +"/"
        + project_name
        + "/"
    ) 
    Team.set_projdir(projdir)
    Team.set_log()

    #woRTA
    # Team.align_check_num = 0
    # Team.mad_num = 0
    # config for framework
    config = model_config()

    model = GPT(config["llm_4o"])
    model_review = GPT(config["llm_4o"])


    # launch project
    team.set_origin_req(project_name, origin_req)

    # 创建不同的角色
    product_manager = Product_Manager(llm=model, llm_review=model_review, team=team)
    architect = Architect(llm=model, llm_review=model_review, team=team)
    projct_manager = Project_Manager(llm=model, llm_review=model_review, team=team)
    programmer = Programmer(llm=model, llm_review=model_review, team=team)
    code_tester = Code_Tester(llm=model, llm_review=model_review, team=team)
    reviewer = Reviewer(target=projct_manager, team=team)

    team.hire_roles(
        product_manager, architect, projct_manager, programmer, code_tester, reviewer
    )
    #
    #
    # ------------------- launch project ------------------------
    team.run()
    # ------------------- launch project ------------------------
    #
    #
    # ------------------- Post Processing --------------------
    # statistics for this process(include team statistics and other information)
    # framework execution end time
    end_time = datetime.now()
    execution_time = end_time - start_time
    total_seconds = execution_time.total_seconds()
    milliseconds = int((total_seconds % 1) * 1000)
    milliseconds_str = str(milliseconds // 10).zfill(2)
    formatted_time = f"{int(total_seconds)}.{milliseconds_str}"
    Team.log.info(
        "\n-----------------\n"
        + team.log_project_stat()
        + "\n-------------------\n"
        + "Execute time: "
        + str(formatted_time)
        + " Seconds"
        + "\n-----------------"
    )
    # ------------------- Post Processing --------------------
    print(
        "\n-----------------\n"
        + team.log_project_stat()
        + "\n-------------------\n"
        + "Execute time: "
        + str(formatted_time)
        + " Seconds"
        + "\n-----------------"
    )


def model_config():
    # loading config for different models, include Qwen and GPT
    config = read_yaml("./0_config/config.yaml")
    dashscope.api_key = config["Qwen"]["api_key"]
    return config


if __name__ == "__main__":
    start_project()
