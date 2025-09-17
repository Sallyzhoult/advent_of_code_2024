from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  
import re


class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day =3)

    def parse_input(self, input_data: str) -> List[int]:

        return input_data

    def part1(self, data: List[int]) -> int:
        pattern = r"mul\((\d{1,3}\,\d{1,3})\)"
        data = re.findall(pattern, "".join(data))
        print (data[:2])
        print(f"Length of data: {len(data)}")
        result = sum( int(x)*int(y) for x, y in (item.split(",") for item in data) )
        return result

    def part2(self, data: List[int]) -> int:
        example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
        data = re.findall(pattern, data)
        print (data[:25])
        enabled = True
        result = 0
        
        for inst in data:
            if inst[0] == "do()":
                enabled = True
            elif inst[0] == "don't()":
                enabled = False
            else:
                if enabled:
                    result += int(inst[1]) * int(inst[2])
        print(f"result: {result}")
        return result

def create_solution():
    return Solution()