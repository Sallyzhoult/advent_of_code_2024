from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    tracking = {}
    def __init__(self):
        super().__init__(day = 11)

    def parse_input(self, input_data: str) -> List[int]:
        testdata = "125 17\n"
        actualdata = input_data
        data = actualdata.strip().split(" ")
        print(data)
        return data

    def part1(self, data: List[int]) -> int:
        # solution without tracking
        """ l = data
        for i in range(0,25):
            l = self.blink(l)           
            #print(f"blink {i} gives {l}")
        return len(l) """
        c = sum([self.blink_r(stone,25) for stone in data])
        return c

    def part2(self, data: List[int]) -> int:
        c = sum([self.blink_r(stone,75) for stone in data])
        return c
            
    def blink(self, data):
        l = []
        for n in data:
            #print(n)
            if n == "0":
                l.append("1")
            elif len(n)%2 == 0:
                mid = len(n)//2
                l.append(n[:mid])
                l.append(str(int(n[mid:])))
            else:
                l.append(str(int(n)*2024))
        return l
    
    def blink_r(self,stone, times):
        
        if times == 0:
            return 1
        if (stone,times) in self.tracking:
            return self.tracking[(stone,times)]
        
        if stone =="0":
            size = self.blink_r("1",times-1)
        elif len(stone)%2 == 0:
            mid = len(stone)//2
            left = str(stone[:mid])
            right = str(int(stone[mid:]))
            size = self.blink_r(left,times-1) + self.blink_r(right,times-1)
        else:
            size = self.blink_r(str(int(stone)*2024),times-1)
        
        if (stone,times) not in self.tracking:
            self.tracking[(stone,times)] = size
            #print(self.tracking)
        return size
            

def create_solution():
    return Solution()