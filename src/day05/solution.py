from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day =5)

    def parse_input(self, input_data: str) -> List[int]:
        rules_origin, data= input_data.split("\n\n")
        #print (rules_origin)
        #print (data)
        rules = {}
        for line in rules_origin.splitlines():
            val, key = map(int, line.split("|"))
            if key not in rules:
                rules[key] = [val]
            else:
                rules[key].append(val)
        #print (rules)
        data =[[int(x) for x in line.split(",")] for line in data.splitlines()]
        #print (data)
        return rules, data

    def part1(self, data: List[int]) -> int:
        # while looking through the sequence, if a number is visited, according to the rules,
        # there are some numbers that should not show up later in the sequence
        # if they do, the sequence is invalid
        # each newly visited number is added to a set of visited numbers and generates a set of forbidden numbers
        
        rules, sequence = data        
        result = 0
        for seq in sequence:
            #print (f"seq: {seq}, visited: {visited}, forbidden: {forbidden}")
            flag = self.is_valid(seq, rules)
            if flag:
                result += seq[(len(seq)-1)//2]

        return result

    def part2(self, data: List[int]) -> int:
        rules, sequence = data        
        result = 0
        for seq in sequence:
            visited = set()
            forbidden = set()
            #print (f"seq: {seq}, visited: {visited}, forbidden: {forbidden}")
            is_invalid = False
            for num in seq:
                if num in forbidden:
                    #print (f"Invalid sequence at number: {num}")
                    is_invalid = True
                    break
                if num not in visited:
                    visited.add(num)
                    if num in rules:
                        for f in rules[num]:
                            forbidden.add(f)
            #if is_invalid:
                #print (f"Invalid sequence: {seq}")

        return result
    
    def is_valid(self, seq: List[int], rules: dict) -> bool:
        visited = set()
        forbidden = set()
        for num in seq:
            if num in forbidden:
                return False
            if num not in visited:
                visited.add(num)
                if num in rules:
                    for f in rules[num]:
                        forbidden.add(f)
        return True
    
def create_solution():
    return Solution()