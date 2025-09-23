from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day =7)

    def parse_input(self, input_data: str) -> List[int]:
        testdata, actualdata = input_data.split("\n\n")
        data = actualdata
        equations =[]
        for line in data.strip().split("\n"):
            #print(line)
            result,operators = line.split(": ")
            equations.append((int(result),[int(i) for i in operators.split()]))
        #print(equations)
        return equations

    def part1(self, data: List[int]) -> int:
        result =[]
        for test_value, ops in data:
            possible_value=[ops[0]]
            for i in range(1,len(ops)):
                op2 = ops[i]
                temp= []
                for p in possible_value:
                    temp.append(p+op2)
                    temp.append(p*op2)
                possible_value = temp
            if test_value in possible_value:
                result.append(test_value)
        return sum(result)
            
        

    def part2(self, data: List[int]) -> int:
        result =[]
        for test_value, ops in data:
            #print(test_value, ops)
            possible_value=[ops[0]]
            for i in range(1,len(ops)):
                op2 = ops[i]
                temp= []
                for p in possible_value:
                    temp.append(p+op2)
                    temp.append(p*op2)
                    temp.append(int(str(p)+str(op2)))
                        
                possible_value = temp
            if test_value in possible_value:
                result.append(test_value)
        return sum(result)

def create_solution():
    return Solution()