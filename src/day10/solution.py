from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  
from collections import defaultdict



class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day = 10)

    def parse_input(self, input_data: str) -> List[int]:
        testdata, actualdata = input_data.split("\n\n")
        data = actualdata.strip().split("\n")
        m = defaultdict(set)
        for i in range(len(data)):
            for j in range(len(data[0])):
                m[int(data[i][j])].add((i,j))
        #print(m)         
        return m

    def part1(self, data: List[int]) -> int:
        s = 0
        steps = [[-1,0],[1,0],[0,1],[0,-1]]
        for h in data[0]:
            sub_t = set()
            to_conquer = [(0,h[0],h[1])]

            while to_conquer:
                current_height, current_r, current_c = to_conquer.pop()
                #print(f"current height: {current_height}, pos:{current_r,current_c}")
                if current_height == 9:
                    sub_t.add((current_r,current_c))
                else:
                    next_height = current_height + 1
                    for step in steps:
                        next_r = step[0] + current_r
                        next_c = step[1] + current_c
                        if (next_r,next_c) in data[next_height]:
                            to_conquer.append((next_height,next_r,next_c))
                            
                            #print(f"can move to height :{next_height} at {(next_r,next_c)}")
                    
            s += len(sub_t)
            #print(f"score for 0 at {h[0],h[1]} is {len(sub_t)}")
        return s
            

    def part2(self, data: List[int]) -> int:
        s = 0
        steps = [[-1,0],[1,0],[0,1],[0,-1]]
        for h in data[0]:
            sub_t = 0
            to_conquer = [(0,h[0],h[1])]

            while to_conquer:
                current_height, current_r, current_c = to_conquer.pop()
                #print(f"current height: {current_height}, pos:{current_r,current_c}")
                if current_height == 9:
                    sub_t +=1
                else:
                    next_height = current_height + 1
                    for step in steps:
                        next_r = step[0] + current_r
                        next_c = step[1] + current_c
                        if (next_r,next_c) in data[next_height]:
                            to_conquer.append((next_height,next_r,next_c))
                            
                            #print(f"can move to height :{next_height} at {(next_r,next_c)}")
                    
            s += sub_t
            #print(f"score for 0 at {h[0],h[1]} is {sub_t}")
        return s

def create_solution():
    return Solution()