import argparse
import importlib
from typing import Optional, List
from datetime import datetime
import sys
from pathlib import Path
from src.common.files import Files

current_path = sys.path[0]
if current_path in sys.path:
    sys.path.remove(current_path)

# Add the src directory to path instead
SRC_PATH = Path(__file__).parent
sys.path.insert(0, str(SRC_PATH))

#print(f"Python path: {sys.path}")  # Debug

def run_solution(day: int, part: Optional[int]):
    # code suggested by copilot
    # print( "in run_solution")
    try:
        module_name = f"day{day:02d}.solution"
        print(f"Importing: {module_name}")
        module = importlib.import_module(module_name)
        
        if hasattr(module, 'create_solution'):
            solution = module.create_solution(day)
            return solution.solve(part)
        else:
            print(f"Day {day}: create_solution function missing")
            return {}   
    except ModuleNotFoundError as e:
        print(f"Day {day} module not found: {e}")
        return {}
    except Exception as e:
        print(f"Error running day {day}: {e}")
        import traceback
        traceback.print_exc()
        return {}
    

    
def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2024 solutions.")
    parser.add_argument("day", type=int, nargs="?", help="Day of the challenge (1-25).")
    parser.add_argument("--part","-p", type=int, choices=[1, 2], help="Part of the challenge (1 or 2).")
    parser.add_argument("--today", "-t",action="store_true", help="Run Today's Puzzle")
    parser.add_argument("--add", action="store_true", help="Optional, create daily file")
    # print(parser.parse_args())
    args = parser.parse_args()
    
    """
    # print(f"Recorded Arguments: {args}")
    print("Python path:", sys.path)
    print("Current directory:", Path.cwd())

    # Check if module exists
    day = 1
    module_path = Path(f"src/day{day:02d}/solution.py")
    print(f"Module exists: {module_path.exists()}")
    print(f"Absolute path: {module_path.absolute()}")
    """
    
    if args.today:
        today = datetime.now()
        print(f"Today's date: {today}")  
        if today.month == 12 and 1 <= today.day <= 25:
            args.day = today.day
            run_solution(args.day, args.part)
        else:
            print("Today is not in the Advent of Code event period (December 1-25).")
            return  
    elif args.day:
        if  not 1 <= args.day <= 25:
            print("Day must be between 1 and 25.")
            return
        elif args.add is True:
            print("Adding day", args.day)
            Files.add_day(args.day)
        
        else:
            print(f"Running Day {args.day}, Part {args.part if args.part else 'Both'}")
            run_solution(args.day, args.part)
            
    else:
        print("Please specify a day (1-25) or use --today to run today's puzzle.")
        return    
    
          
if __name__ == "__main__":
    main()