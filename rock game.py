
import random

w = None
g = None
r = None
y = None
c = None

r = int(input("enter repeat time you want:"))


y = 0
c = 0

for i in range(1,r+1,1):
    g = str(input("choose your sympol(rock,paper,scissor):"))
    words = ("rock", "paper", "scissor")
    w = random.choice(words)
    
    if(g == "rock" and w == "paper"):
        c = c + 1
        print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c  )
    else:
        if(g == "paper" and w == "rock"):
            y = y + 1
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c )
            
        if(g == "paper" and w == "scissor"):
            c = c + 1
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c )
            
        if(g == "scissor" and w == "paper"):
            y = y + 1
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c )
            
        if(g == "scissor" and w == "rock"):
            c = c + 1
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c )
            
        if(g == "rock" and w == "scissor"):
            y = y + 1
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c )
            
        if(g == "rock" and w == "rock"):
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c)
            
        if(g == "paper" and w == "paper"):
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c)
            
        if(g == "scissor" and w == "scissor"):
            print("your choice:",g," --- ", "computer choice:",w,"\nyour score is:" , y ,"\ncomputer score is:" , c)


            
if(y>c):
    print("\n'congratulations, you won :)' ")
    
else:
    print("\n'sorry the computer won :('")

input('\nPress ENTER to exit')

        
    

        













        
