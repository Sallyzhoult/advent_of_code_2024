from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  
import re
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
        V = defaultdict(set)
        pattern = r'p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)'
        for l in data:
            #print(l)
            #print(re.findall(pattern,l))
            s = re.findall(pattern,l)
            i,j,vx,vy = s[0][0],s[0][1],s[0][2],s[0][3]
            
            V[(int(i),int(j))].add((int(vx),int(vy)))
        # print(f"robot init pos are: \n{V}")
        return V

    def part1(self, data: List[int]) -> int:
        w , h , t= 11, 7, 10
        w, h, t = 101, 103, 100
        M = {"tl":0,"tr":0,"bl":0, "br":0}
        
        for p,Vs in data.items():
            #print(Vs)
            for v in Vs:
                next_p_x = (p[0]+v[0]*t) % w
                next_p_y = (p[1]+v[1]*t) % h
                if next_p_x in range(w//2) and next_p_y in range(h//2):
                    M["tl"] += 1
                elif next_p_x in range(w//2) and next_p_y in range(h//2+1,h):
                    M["tr"] += 1
                elif next_p_x in range(w//2+1,w) and next_p_y in range(h//2+1,h):
                    M["br"] += 1
                elif next_p_x in range(w//2+1,w) and next_p_y in range(h//2):
                    M["bl"] += 1
        c= 1
        for k, v in M.items():
            c *=v
            print(f"zone {k} has {v} robots")
        return c

    def part2(self, data: List[int]) -> int:
        w , h = 11, 7
        w, h = 101, 103
        
        
        I = []
        
        filename = "src/day14/day14_frames.txt"
        with open(filename,'w') as f:
            f.write("this is the file to test the frames")
        for i in range(100):
            t = 33+i*103
            G  = [["." for _ in range(w)] for _ in range(h)]
            if i %100 == 0:
                print("current time: ", i)  
            
            for p,Vs in data.items():
                #print(Vs)
                for v in Vs:
                    next_p_x = (p[0]+v[0]*t) % w
                    next_p_y = (p[1]+v[1]*t) % h
                    G[next_p_y][next_p_x] = "#"
            with open(filename,'a') as f:
                f.write(f"time as {t} \n")
                for l in G: 
                    for n in l:
                        f.write(n)
                    f.write("\n")
                    
                    
        
        
        return f"check the file {filename}"
        

def create_solution(day):
    return Solution(day)