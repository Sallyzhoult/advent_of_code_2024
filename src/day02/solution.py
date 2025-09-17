from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion   


class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day =2)

    def parse_input(self, input_data: str) -> List[int]:
        data = []
        for line in input_data.splitlines():
            if line.strip():  # Ensure the line is not empty
                data.append(list(map(int, line.split()))) 
        print(data[:2])          
        return data
    
    def part1(self, data: List[int]) -> int:
        " Solve part 1 of the day's challenge: Find the maximum number."
        
        """ counter_safe =  0
        print(f"Length of data: {len(data)}")
        for row in data:
            #print(f"row: {row}")
            safe_flag= True
            if row[0] < row[1]:
                for i in range(len(row)-1):
                    #print(f"i: {i}, row[i]: {row[i]}, row[i+1]: {row[i+1]}")
                    dist = row[i+1] - row[i]
                    if dist >3 or dist <1:
                        safe_flag = False
                        #print(f"failure at i: {i}, row[i]: {row[i]}, row[i+1]: {row[i+1]}, dist: {dist}")

                        break
                
            elif row[0] > row[1]:
                for i in range(len(row)-1):
                    dist = row[i] - row[i+1]
                    if dist >3 or dist <1:
                        safe_flag = False
                        #print(f"failure at i: {i}, row[i]: {row[i]}, row[i+1]: {row[i+1]}, dist: {dist}")
                        break
            else:
                safe_flag = False
                #print(f"failure at row: {row}")
                continue

            if safe_flag:
                counter_safe += 1
            #print(f"safe_flag: {safe_flag}, counter_safe: {counter_safe}") """
        counter_safe = 0
        for row in data:
            if self.is_safe(row):
                counter_safe += 1
        return counter_safe

    def part2(self, data: List[int]) -> int:
        counter_safe = 0
        for row in data:
            if self.is_safe(row):
                counter_safe += 1
            else:
                for i in range(len(row)):
                    new_row=row[:i] + row[i+1:]
                    if self.is_safe(new_row):
                        counter_safe += 1
                        break

        return counter_safe
    
    def is_safe(self, row: List[int]) -> bool:
        
        differs =[a- b for a, b in zip(row, row[1:])]
        
        is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
        is_inrange = all(1 <= abs(i) <= 3 for i in differs)

        return is_monotonic and is_inrange
def create_solution():
    return Solution()