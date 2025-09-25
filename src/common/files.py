import os, sys
from pathlib import Path

class Files:
    
    @staticmethod
    def get_path():
        
        return path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
    
    @staticmethod
    def add_day(day):
        path = Files.get_path()
        
        folder = os.path.realpath(f"{path}/day{day:02}")
        folder_path = Path(folder)
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            print("Created folder: " + folder)
        
        initfile = os.path.realpath(f"{path}/day{day:02}/__init__.py")
        initfile_path = Path(initfile)  
        if not initfile_path.exists():
            with open(initfile,"w") as f:
                print("Created Init file")
        else:
            print("Module init file exists")
            
        solution = os.path.realpath(f"{path}/day{day:02}/solution.py")
        solution_path = Path(solution)
        if not solution_path.exists():
            base_solution = os.path.realpath(f"{path}/common/solution_example.py")
            with open(base_solution,"r") as content:
                template = content.read()
            with open(solution, "w+") as f:
                f.write(template)
                print("Copied solution template")
        else:
            print("Solution file exists")        
        
        
    