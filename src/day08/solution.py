from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  
from collections import defaultdict


class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day = 8)

    def parse_input(self, input_data: str):
        testdata, actualdata = input_data.split("\n\n")
        data = actualdata.strip().split("\n")
        print(data)
        d_antenna =defaultdict(list)
        for i in range(0,len(data)):
            for j in range(len(data[0])):
                if data[i][j] != ".":
                    d_antenna[data[i][j]].append((i,j))
        print(d_antenna)
        return d_antenna, len(data), len(data[0])

    def part1(self, data) -> int:
        antinode = set()
        d_antenna,n_r, n_c = data
        for a, pos_list in d_antenna.items():   
            for i in range(len(pos_list)-1):
                p1 = pos_list[i]
                for j in range(i+1,len(pos_list)):
                    p2 = pos_list[j]
                    diff_r = p1[0]-p2[0]
                    diff_c = p1[1]-p2[1]
                    if 0<= p1[0] + diff_r<n_r and 0<= p1[1] + diff_c < n_c:
                        antinode.add((p1[0] + diff_r, p1[1] + diff_c))
                    if 0<=p2[0] - diff_r<n_r and 0<= p2[1] - diff_c <n_c: 
                        antinode.add((p2[0] - diff_r, p2[1] - diff_c))
                    #print(f"find antinode for {a} at {p1} and {p2} for {p1[0] + diff_r, p1[1] + diff_c} and {p2[0] - diff_r, p2[1] - diff_c}")
        return len(antinode)   
                
        

    def part2(self, data) -> int:
        antinode = set()
        d_antenna,n_r, n_c = data
        for a, pos_list in d_antenna.items():
            #print(a, pos_list)
            candidates = pos_list
            while candidates:
                p1 = candidates.pop(0)
                antinode.add(p1)
                for p2 in candidates:
                    antinode.add(p2)
                    diff_r = p1[0]-p2[0]
                    diff_c = p1[1]-p2[1]
                    l_n = (p1[0] + diff_r, p1[1] + diff_c)
                    r_n = (p2[0] - diff_r, p2[1] - diff_c)
                    while 0<= l_n[0] < n_r and 0<= l_n[1] < n_c:
                        antinode.add(l_n)
                        l_n=(l_n[0]+ diff_r, l_n[1] + diff_c)
                    while 0<=r_n[0]<n_r and 0<= r_n[1] <n_c: 
                        antinode.add(r_n)
                        r_n = (r_n[0] - diff_r, r_n[1] - diff_c)
            
        return len(antinode) 

def create_solution():
    return Solution()