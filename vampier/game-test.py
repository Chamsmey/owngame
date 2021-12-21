
import tkinter as tk
from tkinter import Label, font
from tkinter.constants import ANCHOR
root=tk.Tk()
root.geometry("1000x700")
frame=tk.Frame()
frame.master.title("GUI")
canvas=tk.Canvas(frame)
bg=tk.PhotoImage(file="image\Bg.png")
label1=Label(root,image=bg)
label1.place(x=0,y=0)
grid=[
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0],
    [0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,2,0,0,0,0,0],
    [0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,3,0],
    [0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,0,0,0] 
    ]
score=0

# def moveWeapon(x1,weapon):
#     canvas.move(weapon,x1+1,0)
#     root.after(1000,lambda:moveWeapon())
##---display------------------------

def dispayScore():
    global score
    scores=canvas.create_text(800,20,text="Your score :"+str(score),font=("",20))
    canvas.create_rectangle(800,40,900,90,fill="red",tags="button")
def draw():
    global grid
    canvas.delete("all")
    x1=0
    x2=60
    y1=0
    y2=60
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==1:
                weapon=canvas.create_rectangle(x1,y2,x2,y1-y1,fill="black")
                # x=x1
                # moveWeapon(x,weapon)
                canvas.create_image(x2-30,y2-30,image=chareacter)
            elif grid[row][col]==2:
                canvas.create_image(x2-30,y2-30,image=enemy)
        
            elif grid[row][col]==3:
                canvas.create_image(x2-30,y2-30,image=food)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,fill="white")
            x1=x2
            x2+=60
        y1=y2
        y2+=60
        x1=0
        x2=60


## -move right --------------------------------------
def moveRight(event):
    global grid,score
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])-1):
            if grid[row][col]==1 and not stop and grid[row][col+1]==2:
                grid[row][col]=0
                grid[row][col+1]=1
                stop=True
                score+=1
            elif grid[row][col]==1 and not stop:
                grid[row][col]=0
                grid[row][col+1]=1
                stop=True
    draw()
    dispayScore()
def moveLeft(event):
    global grid,score
    canvas.delete("all")
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col]==1 )and( not stop) and (col>0) and (grid[row][col-1]==2):
                grid[row][col]=0
                grid[row][col-1]=1
                stop=True
                score+=1
            elif grid[row][col]==1 and not stop and col>0 :
                grid[row][col]=0
                grid[row][col-1]=1
                stop=True
    draw()
    dispayScore()
## -move down --------------------------------------


def moveUp(event):
    global grid,score
    canvas.delete("all")
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==1 and not stop and row>0 and grid[row-1][col]==2:
                grid[row][col]=0
                grid[row-1][col]=1
                stop=True
                score+=1
            elif grid[row][col]==1 and not stop and row>0:
                grid[row][col]=0
                grid[row-1][col]=1
                stop=True
    draw()
    dispayScore()


def moveDown(event):
    global grid,score
    canvas.delete("all")
    stop=False
    for row in range(len(grid)-1):
        for col in range(len(grid[row])):
            if grid[row][col]==1 and not stop and   grid[row+1][col]==2:
                grid[row][col]=0
                grid[row+1][col]=1
                stop=True
                score+=1
            elif grid[row][col]==1 and not stop:
                grid[row][col]=0
                grid[row+1][col]=1
                stop=True
            
    draw()
    dispayScore()
chareacter=tk.PhotoImage(file="image\epiphany.png")
enemy=tk.PhotoImage(file="image\enemy.png")
food=tk.PhotoImage(file="image\ood.png")
## -button --------------------------------------


def button(event):
    draw()
dispayScore()
def message():
    print("hello world")

btn=tk.Button(root,text="button Start",bd="5",command=root.destroy)
canvas.tag_bind("button","<Button-1>",button)
root.bind("<Right>",moveRight)
root.bind("<Left>",moveLeft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()