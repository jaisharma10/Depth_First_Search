## ------------------------------------------------------------------------------------------
#                                  Depth First Search [Obstacle Map]
## ------------------------------------------------------------------------------------------

'''
Author: Jai Sharma
Task: implement Depth First Search [DFS] algorithm on an empty 16 x 8 Maze 
        
--> Path is visualized using pygame. 
    - Start Node is Red
    - Goal Node is Green
    - Solution Path is in Blue/Yellow
    - Explored Nodes are in White
    
--> 4 action steps. Search Sequence 
    1. Up
    2. Right
    3. Down
    4. Left
'''

## ------------------------------------------------------------------------------------------
#                                        Import Libraries
## ------------------------------------------------------------------------------------------

import time
import copy
from collections import deque
import pygame
import sys

start_time = time.time()
print("=======================================================================")

## ------------------------------------------------------------------------------------------
#                                     Node Class
## ------------------------------------------------------------------------------------------

class Node:
    
    '''
    Attributes:
        state: state of the node
        parent: parent of the node
    '''
    
    def __init__(self, state, parent):
        self.state = state     # current node in the tree
        self.parent = parent   # parent of current node
        
    def __repr__(self):         # special method used to represent a class’s objects as string
        return(f'[ state: {self.state}, parent: {self.parent} ]')
    
    def moveUp(self, pos): # Swap node with the node Above
        row, col = pos[0], pos[1]
        if col < 8:  # node above exists
            upNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  # parent is also a Node in form (state, parent)
            upNode.state[0], upNode.state[1]  = row, col + 1
            return(upNode)    # Up is possible
        else:
            return(False)       # Up not possible
    
    def moveDown(self, pos): # Swap node with the node Below
        row, col = pos[0], pos[1]
        if col > 1:  # node below exists
            downNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent)) 
            downNode.state[0], downNode.state[1]  = row, col - 1
            return(downNode)    # Down is possible         
        else:
            return(False)       # Down not possible

    def moveLeft(self, pos): # Swap node with the node on Left
        row, col = pos[0], pos[1]
        if row > 1:  # node to right exists
            leftNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  
            leftNode.state[0], leftNode.state[1]  = row - 1, col
            return(leftNode)    # Left is possible
        else:       
            return(False)       # Left not possible

    def moveRight(self, pos): # Swap node with the node on Right
        row, col = pos[0], pos[1]
        if row < 16: # node to left exists
            rightNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  
            rightNode.state[0], rightNode.state[1]  = row + 1, col
            return(rightNode)    # Right is possible         
        else:
            return(False)       # Right not possible
    
    def getNeighbours(self, pos, visited): # check for neighbours in the 4 directions
        neighbours = []
        up = self.moveUp(pos) 
        down = self.moveDown(pos) 
        left = self.moveLeft(pos) 
        right = self. moveRight(pos) 

        if up: # if Up traversal is valid
            if [up.state[0], up.state[1]] not in visited: # if node up is not explored
                neighbours.append(up)
        if right:
            if [right.state[0], right.state[1]] not in visited:
                neighbours.append(right)
        if down:
            if [down.state[0], down.state[1]] not in visited:
                neighbours.append(down)
        if left:
            if [left.state[0], left.state[1]] not in visited:
                neighbours.append(left)
        return(neighbours)
        

## ------------------------------------------------------------------------------------------
#                                         BFS Function
## ------------------------------------------------------------------------------------------

def dfs(s, g, obsMap):
    
    pygame.init()
    magf = 50 # magnification factor
    screen = pygame.display.set_mode(((17)*magf, (9)*magf))
    hght = 9
    screen.fill((30,30,30))

    startNode = Node(s, None)
    goalNode = Node(g, None)

    queue = deque()               # all neighbour states to explore
    visitedList = []              # all visited states

    # add start node to visited list and queue
    queue.append(startNode)    

    while True:
        
        if not queue:
            currentNode = currentNode.parent
            queue.append(currentNode)
            visitedList.remove(currentNode.state)
            
        currentNode = queue.popleft()  # pop last node 
        
        # Visualize Maze Boundary
        boundary_colour = (0,0, 0)
        boundary_thickness = 35
        pygame.draw.line(screen, boundary_colour, (magf*(0), magf*(hght-0)), (magf*(0), magf*(hght-9)),boundary_thickness)
        pygame.draw.line(screen, boundary_colour, (magf*(0), magf*(hght-9)), (magf*(17), magf*(hght-9)),boundary_thickness)
        pygame.draw.line(screen, boundary_colour, (magf*(17), magf*(hght-9)), (magf*(17), magf*(hght-0)),boundary_thickness)
        pygame.draw.line(screen, boundary_colour, (magf*(17), magf*(hght-0)), (magf*(0), magf*(hght-0)),boundary_thickness)
        
        # Visualize obstacles in Maze
        wall_colour = (80,80,80)
        wall_thickness = 8
        pygame.draw.line(screen, wall_colour, (magf*(2), magf*(hght-1)), (magf*(2), magf*(hght-3)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(2), magf*(hght-5)), (magf*(2), magf*(hght-7)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(5), magf*(hght-5)), (magf*(5), magf*(hght-8)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(2), magf*(hght-3)), (magf*(5), magf*(hght-3)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(2), magf*(hght-5)), (magf*(5), magf*(hght-5)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(2), magf*(hght-7)), (magf*(3), magf*(hght-7)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(7), magf*(hght-2)), (magf*(7), magf*(hght-7)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(9), magf*(hght-4)), (magf*(9), magf*(hght-7)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(11), magf*(hght-4)), (magf*(11), magf*(hght-5)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(12), magf*(hght-1)), (magf*(12), magf*(hght-2)),wall_thickness)
        pygame.draw.polygon(screen, wall_colour, ((magf*(13), magf*(hght-2)),(magf*(13), magf*(hght-3)),(magf*(14), magf*(hght-3)),(magf*(14), magf*(hght-2))))
        pygame.draw.line(screen, wall_colour, (magf*(13), magf*(hght-5)), (magf*(13), magf*(hght-7)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(16), magf*(hght-2)), (magf*(16), magf*(hght-3)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(7), magf*(hght-7)), (magf*(15), magf*(hght-7)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(9), magf*(hght-4)), (magf*(11), magf*(hght-4)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(9), magf*(hght-2)), (magf*(14), magf*(hght-2)),wall_thickness)
        pygame.draw.line(screen, wall_colour, (magf*(13), magf*(hght-5)), (magf*(16), magf*(hght-5)),wall_thickness)

        # Visualize Start Node and End Node
        pygame.draw.circle(screen, (0,128,0), (magf*(goalNode.state[0]), magf*(9-goalNode.state[1])), 16)   # Goal Node
        pygame.draw.circle(screen, (255,0,0), (magf*(startNode.state[0]), magf*(9-startNode.state[1])), 16) # Start Node
        pygame.display.update()
        
        if currentNode.state not in obsMap:                  # if current node is not in Obstacle Space
            if currentNode.state not in visitedList:         # new state is not goal state and not in visited list
                position = currentNode.state                 # [x,y] of current node, same as state
                visitedList.append((currentNode.state))
                
                pygame.draw.circle(screen, (255,255,255), (1 + magf*(currentNode.state[0]), magf*(9-currentNode.state[1])), 7)   # Current Node
                pygame.display.update()
                time.sleep(0.15)

                if currentNode.state == g:  # check if goal state reached
                    print("Goal Reached! Backtracked Path is:") 
                    backTrackList = backtrack(currentNode, startNode)  # backtrack list is goal to start
                    reversed_backTrackList = backTrackList[::-1] # reversed --> list is start to goal
                    print(backTrackList)
                    prev = reversed_backTrackList[0]

                    for route in reversed_backTrackList:   # visualize the solution path
                        pygame.draw.circle(screen, (0,0,250), (magf*(route[0]), magf*(9 - route[1])), 7)   # Current Node     
                        pygame.draw.line(screen, (255, 255, 0), (magf*(route[0]), magf*(9 - route[1])), (magf*(prev[0]), magf*(9 - prev[1])),5)
                        pygame.draw.circle(screen, (0,0,250), (magf*(prev[0]), magf*(9-prev[1])), 7)   # Current Node     
                        pygame.display.update()
                        prev = route
       
                    time.sleep(10) # show screen for these number of seconds
                    break
                
                else: # if not goal, add neigbours to queue
                    Neighbours = currentNode.getNeighbours(position, visitedList)  # get next layer
                    for child in reversed(Neighbours):
                        if child not in queue:
                            if child.state not in visitedList:
                                queue.appendleft(child)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    return(None)
        
        
## ------------------------------------------------------------------------------------------
#                                  Helper Functions
## ------------------------------------------------------------------------------------------

def backtrack(current, start):
    backtrackList = [current.state]   # new list to collect backtracked list
    while(current.state != start.state):
        current = current.parent
        backtrackList.append(current.state)
    return(backtrackList)

def buildMap(mapHeight, mapWidth):
    mapCord = []
    obsCord = []
    
    for x in range(1, mapWidth + 1, 1):
        for y in range(1, mapHeight + 1,1):
            mapCord.append([x,y])

    for x,y in mapCord: 
        # Vertical Walls
        if (x == 2) and (y <= 7) and (y >= 5):  # Wall 1
            obsCord.append([x,y])    
        if (x == 2) and (y <= 3) and (y >= 1):  # Wall 2
            obsCord.append([x,y]) 
        if (x == 5) and (y <= 8) and (y >= 5):  # Wall 3
            obsCord.append([x,y]) 
        if (x == 7) and (y <= 7) and (y >= 2):  # Wall 4
            obsCord.append([x,y]) 
        if (x == 9) and (y <= 7) and (y >= 4):  # Wall 5
            obsCord.append([x,y])             
        if (x == 11) and (y <= 5) and (y >= 4):  # Wall 6
            obsCord.append([x,y])
        if (x == 12) and (y <= 2) and (y >= 1):  # Wall 7
            obsCord.append([x,y])              
        if (x == 13) and (y <= 7) and (y >= 5):  # Wall 8
            obsCord.append([x,y])   
        if (x == 16) and (y <= 3) and (y >= 2):  # Wall 9
            obsCord.append([x,y])               
        if (x == 13) and (y <= 3) and (y >= 2):  # Wall 10
            obsCord.append([x,y])   
        if (x == 14) and (y <= 3) and (y >= 2):  # Wall 11
            obsCord.append([x,y]) 
        # Horizontal Walls        
        if (x <= 5) and (x >= 2) and (y == 3):  # Wall 1
            obsCord.append([x,y])
        if (x <= 5) and (x >= 2) and (y == 5):  # Wall 2
            obsCord.append([x,y])
        if (x <= 3) and (x >= 2) and (y == 7):  # Wall 3
            obsCord.append([x,y])
        if (x <= 14) and (x >= 9) and (y == 2):  # Wall 4
            obsCord.append([x,y])
        if (x <= 11) and (x >= 9) and (y == 4):  # Wall 5
            obsCord.append([x,y])
        if (x <= 15) and (x >= 7) and (y == 7):  # Wall 6
            obsCord.append([x,y])
        if (x <= 16) and (x >= 13) and (y == 5):  # Wall 7
            obsCord.append([x,y])

    return(mapCord,obsCord)
            
        
## ------------------------------------------------------------------------------------------
#                                       Main Function
## ------------------------------------------------------------------------------------------

if __name__== "__main__":
    
    s = [1,4] # Start State
    g = [16,4] # Goal State

    # Map Size is set as:
    mapWidth = 16
    mapHeight = 8  
      
    # Build a Map
    mapCord, obsCord = buildMap(mapHeight, mapWidth)
    
    # checks if inputs are Valid
    if s not in mapCord:
        print("Start Node outside Map")
    elif g not in mapCord:
        print("Goal Node outside Map")
    elif s in obsCord:
        print("Start Node inside Map")
    elif g in obsCord:
        print("Goal Node inside Map")
    elif s == g: # Check if start node is goal node
        print("Start node is Goal Node!!")
    else: 
        print("Implementing Depth First Search")
        print("===============================================================================================")
        dfs(s, g, obsCord)
    
## ------------------------------------------------------------------------------------------
#                                Display --> Forward and Backward Path
## ------------------------------------------------------------------------------------------

end_time = time.time()

print("===============================================================================================")
print("Time to Find Solution Path", round((end_time - start_time), 3), "seconds")
print("===============================================================================================")

print('\n')
