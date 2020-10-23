# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:24:27 2020
@author: Tristan Nibbe and Luis Figueroa
"""

def printPath(path):
  for i in range(len(path)-1,-1,-1):
    print("->" + str(path[i]),end="")

class MoveNode:

  def __init__(self,parent,location,direction):
    self.parent = parent
    self.location = location
    self.direction = direction

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
            #print("moving down")
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
            
            #print("moving up")
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
            
            #print("moving right")
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
            #print("moving left")
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
         
	#creates a node to represent a movement choice, takes the direction that was made to get here and the node that that movement was made from
    def createMoveNode(self,parent,direction):
      newMove = self.move_direction(direction,parent.location)
      newNode = MoveNode(parent,newMove[1],direction)
      return newNode

	#tests if two locations are equal
    def areLocsEqual(self,locationOne,locationTwo):
      if locationOne.x == locationTwo.x and locationOne.y == locationTwo.y:
        return True
      else:
        return False

	#creates a move node for up down left and right of the entered node, removing any that end up being equal to the parent because this means that is not a valid move
    def createMoveNodeList(self,parent):
        leftNode = self.createMoveNode(parent,"left")
        rightNode = self.createMoveNode(parent,"right")
        upNode = self.createMoveNode(parent,"up")
        downNode = self.createMoveNode(parent,"down")

        moveList = [leftNode,rightNode,upNode,downNode]

        for node in moveList:
          if(self.areLocsEqual(node.location,parent.location) == True):
            moveList.remove(node)
        return moveList
	
	#takes a node, returns the path that the start node took to reach that node
    def returnPath(self,endNode):
      currNode = endNode
      path = []
      while currNode.parent != None:
        path.append(currNode.direction)
        currNode = currNode.parent
      return path

    def find_solution(self):
        goal_loc = self.find_location_of("D")
        currNode = MoveNode(None,self.find_location_of("R"),None)
        moveList = []
        
        while(self.areLocsEqual(currNode.location,goal_loc) == False):
          newMoveList = self.createMoveNodeList(currNode)
          for node in newMoveList:
            moveList.append(node)

          currNode = moveList.pop(0)

        path = self.returnPath(currNode)
        return(path)
    
    
board =     [['1','1','1','1','1','1','1','1','1'],
             ['1','0','0','0','1','0','0','0','1'],  
             ['1','0','0','0','1','0','0','R','1'],
             ['1','0','0','0','0','0','0','0','1'],
             ['1','0','0','0','0','1','0','0','1'],
             ['1','1','1','0','0','1','0','0','1'],
             ['1','1','1','0','0','1','1','1','1'],
             ['1','1','0','0','0','0','0','D','1'],
             ['1','1','1','1','1','1','1','1','1']]


myRobotMaze = RobotMaze(board)
path = myRobotMaze.find_solution()
printPath(path)