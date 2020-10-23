# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:24:27 2020

@author: Tristan Nibbe and Luis Figueroa
"""
import random
class RobotMaze():
    
    class Location():
        
        def __init__(self,x_coordinate= None,y_coordinate=None):
            self.x=x_coordinate
            self.y=y_coordinate
    
    
    def __init__(self,board):
        self.board = board
        self.directions=["up","down","right","left"]
        self.goal_location =self.find_location_of("D")
        self.fringe = None
    
    def print_board(self, board):
        for i in range(len(board)):
            print(board[i])
    
    '''Param: char   Return: Location(x,y)
    pass the character of the object you are trying to find on the board
    returns the location of that object (EX: D or R)'''
    def find_location_of(self,letter):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j]==letter):
                    goal_location = self.Location(i,j)
                    return goal_location
    
    '''Param: String,Location(x,y)    Return: Location(x,y)
    robot moves in the direction it was directed and will stop when
    it finds a 1 in the next cell or when it is on the Diamond location'''
    def move_direction(self,direction,current_location):
        
        temp = self.board.copy()
        stop_reason = ""
        
        if(direction =="down"):
            print("moving down")
            for i in range(current_location.x,len(self.board)):
                if(temp[i][current_location.y]=="D"):
                    stop_reason="goal"
                    stop_location = self.Location(i,current_location.y)
                    break
                elif(temp[i+1][current_location.y]=="1"):
                    stop_reason="wall"    
                    stop_location = self.Location(i,current_location.y)
                    break
                    
        elif(direction=="up"):
            
            print("moving up")
            for i in range(current_location.x,-1,-1):
                
                if(temp[i][current_location.y]=="D"):
                    stop_reason="goal"
                    stop_location = self.Location(i,current_location.y)
                    break
                elif(temp[i-1][current_location.y]=="1"):
                    stop_reason="wall"
                    stop_location = self.Location(i,current_location.y)
                    break
                    
           
        elif(direction =="right"):
            
            print("moving right")
            for i in range(current_location.y,len(self.board)):
                
                if(temp[current_location.x][i]=="D"):
                    stop_reason="goal"
                    stop_location = self.Location(current_location.x,i)
                    break
                elif(temp[current_location.x][i+1]=="1"):
                    stop_reason="wall"
                    stop_location = self.Location(current_location.x,i)
                    break
                            
        else:
            print("moving left")
            for i in range(current_location.y,-1,-1):
                if(temp[current_location.x][i]=="D"):
                    stop_reason="goal"
                    stop_location = self.Location(current_location.x,i)
                    break
                elif(temp[current_location.x][i-1]=="1"):
                    stop_reason="wall"
                    stop_location = self.Location(current_location.x,i)
                    break
                
                
        return (stop_reason,stop_location)
            
    
    def find_solution(self):
        
        
        robot_location = self.find_location_of("R")
        print(f"Location of robot X:{robot_location.x} Y:{robot_location.y}")
        print(f"Goal X:{self.goal_location.x} Y:{self.goal_location.y}")
       
        (reason, stop_loc )= self.move_direction("left", robot_location)
        print(f"stop @ X:{stop_loc.x} Y:{stop_loc.y}  Reason:{reason}\n")
            
        (reason, stop_loc )= self.move_direction("down", robot_location)
        print(f"stop @ X:{stop_loc.x} Y:{stop_loc.y}  Reason:{reason}\n")


        pass
    
    
board = [['1','1','1','1','1','1','1','1','1'],
             ['1','0','0','0','1','0','0','0','1'],  
             ['1','0','0','0','1','0','0','R','1'],
             ['1','0','0','0','0','0','0','0','1'],
             ['1','0','0','0','0','1','0','0','1'],
             ['1','1','1','0','0','1','0','D','1'],
             ['1','1','1','0','0','1','1','1','1'],
             ['1','1','0','0','0','0','0','D','1'],
             ['1','1','1','1','1','1','1','1','1']]


myRobotMaze = RobotMaze(board)
myRobotMaze.find_solution()
