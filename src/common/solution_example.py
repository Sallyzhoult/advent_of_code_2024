from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    # from day 12, the solution template has been updated 
    # so that the day argument doesn't need to be added everyday with super function
    """ def __init__(self):
        super().__init__(day =???)
 """
    def parse_input(self, input_data: str) -> List[int]:
        try:
            testdata, actualdata = input_data.split("\n\n")
        except:
            print("!!Warning: test data is not added to the input")
            return
        data = actualdata
        return data

    def part1(self, data: List[int]) -> int:
        pass

    def part2(self, data: List[int]) -> int:
        pass

def create_solution(day):
    return Solution(day)