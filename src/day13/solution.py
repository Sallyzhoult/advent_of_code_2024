from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  
import re


class Solution(BaseSolutionDecoratorVersion):
    # from day 12, the solution template has been updated 
    # so that the day argument doesn't need to be added everyday with super function
    """ def __init__(self):
        super().__init__(day =???)
 """
    def parse_input(self, input_data: str) -> List[int]:
        
        """ try:
            testdata, actualdata = input_data.split("\n\n")
        except:
            print("!!Warning: test data is not added to the input")
            return """
        input_data = input_data.strip().split("\n\n")
        machine = {}
        btn_As= []
        btn_Bs =[]
        prizes=[]
        for m in input_data:
            m = m.split("\n")
            #print(m)
            
            btn_A = tuple([int(i) for i in re.findall(r'X\+(\d+), Y\+(\d+)',m[0])[0]])
            #print(btn_A)
            btn_As.append(btn_A)
            btn_B = tuple([int(i) for i in re.findall(r'X\+(\d+), Y\+(\d+)',m[1])[0]])
            #print(btn_B)
            btn_Bs.append(btn_B)
            prize = tuple([int(i) for i in re.findall(r'X\=(\d+), Y\=(\d+)',m[2])[0]])
            
            #print(prize)
            prizes.append(prize)
        
        return btn_As, btn_Bs, prizes

    def part1(self, data: List[int]) -> int:
        btn_As, btn_Bs, prizes = data
        t = 0
        for i in range(len(btn_As)):
            A = btn_As[i]
            B = btn_Bs[i]
            p = prizes[i]
            #print(f'p:{p}, A:{A}, B:{B}')
            
            l = -1, 0
            for j in range(101):
                for k in range(101):
                    cost  = 3*j + k
                    pos = A[0]*j + B[0]*k, A[1]*j + B[1]*k
                    if pos == p:
                        if l[0]== -1:
                            l = 0,cost
                        else:
                            l[1] = min(l[1], cost)
                        #print(f"find one cost for {cost}")
            if l[0]== 0:
                t+= l[1]  
                   
                
        return t
    
              
    
        
            

    def part2(self, data: List[int]) -> int:
        btn_As, btn_Bs, prizes = data
        t = 0
        for i in range(len(btn_As)):
            A = btn_As[i]
            B = btn_Bs[i]
            
            p = prizes[i][0]+10000000000000, prizes[i][1]+10000000000000
            #print(f'p:{p}, A:{A}, B:{B}')
            
            d = A[0]*B[1]-A[1]*B[0]
            if d != 0:
                x = (p[0]*B[1]-p[1]*B[0])/d
                y = (p[1]*A[0]-p[0]*A[1])/d
                #print("steps are ",x,y)
            if x == int(x) and y == int(y):
                t+= int(3*x+y)
                #print("win")  
               
                
        return t

def create_solution(day):
    return Solution(day)