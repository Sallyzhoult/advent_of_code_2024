from typing import List, Tuple
from common.base_solution_decorator_version import BaseSolutionDecoratorVersion  
from collections import defaultdict


class Solution(BaseSolutionDecoratorVersion):
    def __init__(self):
        super().__init__(day = 6)

    def parse_input(self, input_data: str):
        test_data, actual_data = input_data.split("\n\n")
        o_pos = set()
        data = actual_data
        
        data = data.splitlines()
        n_r= len(data)
        n_c = len(data[0])
        
        for i in range(n_r):
            for j in range(n_c):
                if data[i][j] =="#":
                    o_pos.add((i,j))
                elif data[i][j] !=".":
                    print(f"Guard starts at {i},{j}, as {data[i][j]}")
                    g_direction = (i,j,data[i][j])
        #print (f"o_pos: {o_pos}")
        return o_pos,n_r,n_c, g_direction

    def part1(self, data) -> int:
        is_exit, visited, visited_entries = self.patrol(data)
        return len(visited)
    
    def part2(self, data) -> int:
        _,_,_,(i,j,_) = data
        startpos = (i,j)
        is_exit, visited, visited_entries = self.patrol(data)
        #print(visited)
        visited_entries.pop(startpos)
        loop_cnt= 0

        for i, j in visited:
            is_exit_copy,_,_= self.patrol(data,(i,j))
            if not is_exit_copy:
                loop_cnt+=1
        
        return loop_cnt
    
    #inspired by other peoples solution
    
    def patrol(self,data, new_obstacle = None):
        o_pos,n_r,n_c, g_direction = data
        current_r, current_c, direction = g_direction
        
        visited = set()
        visited.add((current_r, current_c))
        
        visited_entries={}

        directions = ((-1,0),(0,1),(1,0),(0,-1))
        direction_idx = {"^":0, ">":1, "v":2, "<":3}
        idx = direction_idx[direction]

        while True:
            dr, dc = directions[idx]
            next_r, next_c = current_r + dr, current_c + dc
            
            if next_r <0 or next_r >= n_r or next_c <0 or next_c >= n_c:
                # we are going to exit the grid
                #print(f"new obstacle in {new_obstacle}, leaving at { current_r,current_c}")
                return True, visited, visited_entries
            
            if (next_r, next_c) in o_pos or (next_r, next_c) == new_obstacle:
                # hit an obstacle, turn right
                idx = (idx + 1) % 4
                #print(f"change direction at ", current_r, current_c)
                continue
            else:
                current_r, current_c = next_r, next_c
                visited.add((current_r, current_c))
                if (current_r, current_c) not in visited_entries:
                    visited_entries[(current_r, current_c)] = idx
                elif visited_entries[(current_r, current_c)] == idx:
                    # we have been here before with the same direction, we are in a loop
                    #print(f"new obstacle in {new_obstacle},find a loop")
                    return False, None, None
            

    # this is my solution for patrol
    """ def patrol(self,data):
        o_pos_r, o_pos_c, n_r, n_c, g_direction = data
        current_r, current_c, direction = g_direction
        visited = defaultdict(set)
        visited[current_r, current_c].add(direction)
        next_direction_dict = {"^":">", "v":"<", "<":"^", ">":"v"}
        
        while 0<current_r<n_r-1 and 0<current_c<n_c-1:
            # check if has visited this position and direction
            # If we have visited this position and direction, we are in a loop
            # check if next position is an obstacle
            if direction =="^":                
                    
                if current_c in o_pos_r[current_r-1]:
                    direction = next_direction_dict[direction]
                    #print (f"Hit an obstacle at {current_r},{current_c}, new direction {direction}")
                else:
                    current_r -=1
            elif direction =="v":
                
                if current_c in o_pos_r[current_r+1]:
                    direction = next_direction_dict[direction]
                    #print (f"Hit an obstacle at {current_r},{current_c}, new direction {direction}")
                else:
                    
                    current_r +=1
            elif direction =="<":
                
                if current_r in o_pos_c[current_c-1]:
                    direction = next_direction_dict[direction]
                    #print (f"Hit an obstacle at {current_r},{current_c}, new direction {direction}")
                else:
                    current_c -=1
            elif direction ==">":
                
                if current_r in o_pos_c[current_c+1]:
                    direction = next_direction_dict[direction]
                    #print (f"Hit an obstacle at {current_r},{current_c}, new direction {direction}")
                else:
                    
                    current_c +=1
            else:
                print (f"Direction error: {direction}")
                break
            visited[(current_r, current_c)].add(direction)
        #print("Exited the grid at ", current_r, current_c)
        return len(visited) """
def create_solution():
    return Solution()