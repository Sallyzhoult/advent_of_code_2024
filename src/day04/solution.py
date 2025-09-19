from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day = 4)

    def parse_input(self, input_data: str) -> List[int]:
        data = list(map(str, input_data.splitlines()))
        #print(data)
        return data

    def part1(self, data: List[int]) -> int:
        # locgic is to covert the sheet to four sets and check sequence so XMAS
        x_set, m_set, a_set, s_set = self.re_arrange(data)
        
        counter = 0
        for (x_r,x_c) in x_set:
            # check right
            if (x_r, x_c+1) in m_set and (x_r, x_c+2) in a_set and (x_r, x_c+3) in s_set:
                counter += 1
            # check down
            if (x_r+1, x_c) in m_set and (x_r+2, x_c) in a_set and (x_r+3, x_c) in s_set:
                counter += 1
            # check diag down right
            if (x_r+1, x_c+1) in m_set and (x_r+2, x_c+2) in a_set and (x_r+3, x_c+3) in s_set:
                counter += 1
            # check diag down left
            if (x_r+1, x_c-1) in m_set and (x_r+2, x_c-2) in a_set and (x_r+3, x_c-3) in s_set:
                counter += 1    
            # check left
            if (x_r, x_c-1) in m_set and (x_r, x_c-2) in a_set and (x_r, x_c-3) in s_set:
                counter += 1    
            # check up
            if (x_r-1, x_c) in m_set and (x_r-2, x_c) in a_set and (x_r-3, x_c) in s_set:
                counter += 1    
            # check diag up right
            if (x_r-1, x_c+1) in m_set and (x_r-2, x_c+2) in a_set and (x_r-3, x_c+3) in s_set:
                counter += 1
            # check diag up left
            if (x_r-1, x_c-1) in m_set and (x_r-2, x_c-2) in a_set and (x_r-3, x_c-3) in s_set:
                counter += 1
        return counter

    def part2(self, data: List[int]) -> int:
        x_set, m_set, a_set, s_set = self.re_arrange(data)
        
        Counter = 0
        for (a_r, a_c) in a_set:
            if (a_r-1, a_c-1) in m_set and (a_r+1, a_c+1) in s_set:
                if (a_r-1, a_c+1) in m_set and (a_r+1, a_c-1) in s_set:
                    Counter += 1
                if (a_r-1, a_c+1) in s_set and (a_r+1, a_c-1) in m_set:
                    Counter += 1
            if (a_r-1, a_c-1) in s_set and (a_r+1, a_c+1) in m_set:
                if (a_r-1, a_c+1) in m_set and (a_r+1, a_c-1) in s_set:
                    Counter += 1
                if (a_r-1, a_c+1) in s_set and (a_r+1, a_c-1) in m_set:
                    Counter += 1
        return Counter
    
    def re_arrange(self, data: List[int]) -> Tuple[set, set, set, set]:
        x_set=set()
        m_set=set()
        a_set=set()
        s_set=set()

        for r in range(len(data)):
            for c in range(len(data[r])):
                char = data[r][c]
                if char == 'X':
                    x_set.add((r,c))
                elif char == 'M':
                    m_set.add((r,c))
                elif char == 'A':
                    a_set.add((r,c))
                elif char == 'S':
                    s_set.add((r,c))

        return x_set, m_set, a_set, s_set

def create_solution():
    return Solution()