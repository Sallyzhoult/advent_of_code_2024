from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  



class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day =9)

    def parse_input(self, input_data: str) -> List[int]:
        testdata, actualdata = input_data.split("\n\n")
        data = actualdata.strip()
        print(len(data))
        return data

    def part1(self, data: List[int]) -> int:
        d_string = {}
        pos = 0
        for i in range(len(data)):
            for j in range(int(data[i])):
                if i%2:
                    d_string[pos] ="." 
                else:
                    d_string[pos] = i//2 
                pos += 1
        #print(d_string)
        
        p_h = 0
        p_t = len(d_string)-1
        while d_string[p_h] != ".":
            p_h +=1
        while p_h < p_t:   
            d_string[p_t],d_string[p_h] = d_string[p_h], d_string[p_t]
            while d_string[p_h] != ".":
                p_h +=1
            while d_string[p_t] ==".":
                p_t -=1   
            
        
        #print ("".join([str(i) for _,i in d_string.items()]))   
        s = sum([k*int(v) for k, v in d_string.items() if v != "."])
        
        return s

    def part2(self, data: List[int]) -> int:
        file = {}
        space = {}
        pos = 0
        for i in range(len(data)):
            if i%2 :
                space[i//2] = [pos, int(data[i])]
            else:
                file[i//2] = [pos, int(data[i])]
            pos += int(data[i])
        #print(file)
        #print(space)
        s= 0
        for f_id in range(len(file)-1,0,-1):
            #print (f"checking file {f_id}")
            for s_id in range(0,f_id):
                #print (f"checking file {f_id} and space {s_id}")
                if not space[s_id][1]:
                    continue
                if space[s_id][1]>= file[f_id][1]:
                    file[f_id][0] = space[s_id][0]
                    space[s_id][1] -=file[f_id][1]
                    space[s_id][0] +=file[f_id][1]
                    break
            s += (2*file[f_id][0] +file[f_id][1]-1)*file[f_id][1]//2 * f_id
                    
        #print("after compressed")
        #print(f"file dict: {file}")
        #print(f"space dict: {space}") 
        
        
        return s

def create_solution():
    return Solution()