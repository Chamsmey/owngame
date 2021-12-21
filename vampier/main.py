# 
# Exercise 1
# 
# 
# array2D=[
#     [6,4,5],
#     [4,5,6],
#     [5,6,4]
# ]
# isMagic=True
# trueNumber=0
# numberDicoLeft=0
# numberDicoRight=0
# number=0
# for col in range(len(array2D[0])):
#     trueNumber+=array2D[0][col]
# for row in range(len(array2D)):
#     number=len(array2D[row])-1
#     numberDicoLeft+=array2D[row][row]
#     numberRow=0
#     numberCol=0 
#     for col in range(len(array2D[row])):
#         numberCol+=array2D[row][col]
#         numberRow+=array2D[col][row]

#     numberDicoRight+=array2D[row][number-row]
#     if numberCol!=trueNumber or numberRow!=trueNumber:
#         isMagic=False

# if numberDicoLeft!=trueNumber or numberDicoRight!=trueNumber:
#     isMagic=False
# print(isMagic)
# if isMagic:
#     print("This is magic square:")
# else:
#     print("This is not magic square")
# print(array2D)
#exercise 2
# characters=[
#     [0,"D",0],
#     [0,0,0,0],
#     [0,0,0,0]
# ]
# moveAction=input()
# move=True
# if moveAction=="L" or moveAction=="R":
#     for char in range(len(characters)):
#         for value in range(len(characters[char])):
import tkinter as tk
root=tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("Game vampire")
canvas=tk.Canvas(frame)

bord_size = 5

def board(x, y):
    board_string = ""
    for row in range(bord_size):
        for col in range(bord_size):
            if(row == x and col == y):
                board_string += "D "
            else:
                board_string += "0 "
        board_string += "\n"
    return board_string

p  = [3,2]
x = p[0]
y = p[1]
print (board(p[0], p[1]))

while (x>=0 and x<5) or (y>=0 and y<5) :
    txt = input()
    if (txt.upper() == "L"):
        if (y>0 and y<=4):
            y -= 1
           
    elif (txt.upper() == "R"):
        if (y>=0 and y<4):
            y += 1
           
    elif (txt.upper() == "D"):
        if (x>=0 and x<4):
            x += 1
            
    elif (txt.upper() == "U"):
        if (x>0 and x<=4):
            x -= 1
    print(board(x, y))
print("Lost")
