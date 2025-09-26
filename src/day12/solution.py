from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion
from collections import defaultdict



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
        data = actualdata.strip().split("\n")
        return data

    def part1(self, data: List[int]) -> int:
        
        D = [[-1,0],[1,0],[0,1],[0,-1]]
        V = set()
        c = 0
        n_r = len(data)
        n_c = len(data[0])
        for i in range(n_r):
            for j in range(n_c):
                if (i, j) in V:
                    continue
                q = [(i,j)]
                l = data[i][j]
                s = set()
                while q:
                    ii,jj = q.pop()
                    #print(f"for {l} inspecting {ii},{jj}")
                    if (ii,jj) in s:
                        continue
                    s.add((ii,jj))
                    for d in D:
                        x, y = ii+d[0], jj+d[1]
                        
                        if x in range(n_r) and y in range(n_c) and data[x][y] == l:
                            q.append((x,y))
                A = len(s)
                P = 0
                for (x,y) in s:
                    for (dr,dc) in D:
                        if (x+dr,y+dc) not in s:
                            P += 1
                c += A*P
                print(f"for area of {l} it covers {s} with a boundary of {P} and area of {A}")
                V.update(s)
        return c
                
                
                
        
                
                
    def part2(self, data: List[int]) -> int:
        pass

def create_solution(day):
    return Solution(day)