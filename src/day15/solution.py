from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    # from day 12, the solution template has been updated 
    # so that the day argument doesn't need to be added everyday with super function
    """ def __init__(self):
        super().__init__(day =???)
 """
    def parse_input(self, input_data: str) -> List[int]:
        m,instructions = input_data.strip().split("\n\n")
        print(instructions)
        instructions = "".join(instructions.split("\n"))
        print(instructions)
        m_d = {}
        m = m.strip().split("\n")
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]== "@":
                    startpos = (i,j)
                    print(startpos)
                    m_d[(i,j)]="."
                else:
                    m_d[(i,j)]=m[i][j]
        for i in range(len(m)):
            for j in range(len(m[0])):
                print(m_d[(i,j)],end="")    
            print("")              
        return startpos, m_d, instructions

    def part1(self, data: List[int]) -> int:
        pass

    def part2(self, data: List[int]) -> int:
        pass

def create_solution(day):
    return Solution(day)