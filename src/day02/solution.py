from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion   


class Solution(BaseSolutionDecoratorVersion):
    def __init__(self, day: int = 1):
        super().__init__(day)
        
    def parse_input(self, input_data: str) -> List[int]:
        leftlist =[]
        rightlist =[]
        
        for line in input_data.splitlines():
            if line.strip():  # Ensure the line is not empty
                left, right = map(int, line.split())
                leftlist.append(left)
                rightlist.append(right)
                
        return leftlist, rightlist
    
    def part1(self, data: List[int]) -> int:
        " Solve part 1 of the day's challenge: Find the maximum number."
        
        return 
    
    def part2(self, data: List[int]) -> int:
        pass
        
    
def create_solution():
    return Solution()