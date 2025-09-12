import requests
from typing import Optional,List, Tuple
from pathlib import Path
from datetime import datetime


def get_input(day: int, use_cache: bool = True) -> str:
    " get input data from local file or download from Advent of Code website. "
    
    
    input_path = Path(f"inputs/day{day:02d}.txt")
    
    if use_cache and input_path.exists():
        print(f"Using cached input for day {day} from {input_path}")
        with open(input_path, 'r') as file:
            return file.read()

    session_token = "53616c7465645f5feb766218916056426050e53491ae4bcfe2935600ad3af30ccc28e4ccff34b92c4095e92defd143c34b73699e04b8a3f9d3ea89ec9ca6afb3"

    if not session_token:
        raise ValueError("Session token not found. Please set the AOC_SESSION environment variable.")

    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {"Cookie": f"session={session_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Downloaded input for day {day} and saved to {input_path}")
        with open(input_path, 'w') as file:
            file.write(response.text)
        return response.text
    else:
        raise ValueError("Failed to retrieve input data.")
    
    