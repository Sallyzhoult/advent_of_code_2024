from abc import ABC, abstractmethod
from typing import Any, Optional
from datetime import datetime
from common.input_utils import get_input



class BaseSolutionDecoratorVersion(ABC):
    
    def __init__(self, day: int):
        self.day = day
        self.input_data = None
        
    def load_input(self) -> str:
        " Load input data from a file corresponding to the day."
        print(f"current self.day: {self.day}")
        if self.input_data is None:
            self.input_data = get_input(self.day)  # function to be defined
        return self.input_data
    
    @abstractmethod
    def parse_input(self, input_data: str) -> Any:
        " Parse the raw input data into a suitable format."
        pass
    
    @abstractmethod
    #@timer 
    def part1(self, data:Any) ->Any:
        " Solve part 1 of the day's challenge."
        pass
    
    @abstractmethod
    #@timer
    def part2(self, data:Any) -> Any:
        " Solve part 2 of the day's challenge."
        pass
    
    def solve(self, part: Optional [int] = None) -> dict:
        " Solve the specified part of the challenge, or both if part is None."
        print("start to solve")
        input_data = self.load_input()
        parsed_data = self.parse_input(input_data)
        
        result = {}
        if part == 1 or part is None:
            result['part1'] = self.part1(parsed_data)
            print (f"Day {self.day} Part 1: {result['part1']}")
        
            
        if part == 2 or part is None:
            result['part2'] = self.part2(parsed_data)
            print (f"Day {self.day} Part 2: {result['part2']}")
            
        return result