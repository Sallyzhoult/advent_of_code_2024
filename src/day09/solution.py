from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day =9)

    def parse_input(self, input_data: str) -> List[int]:
        testdata, actualdata = input_data.split("\n\n")
        data = actualdata
        return data

    def part1(self, data: List[int]) -> int:
        pass

    def part2(self, data: List[int]) -> int:
        pass

def create_solution():
    return Solution()