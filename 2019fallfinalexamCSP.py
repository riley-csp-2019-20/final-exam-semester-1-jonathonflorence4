#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name jonathon florence
#
#Date
# december 18 2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl




#create turtle
neo= trtl.Turtle() 
turtlesize= 10

 




#movement functions
def up():
    neo.setheading(90)
    neo.forward(10)


def down():
    neo.setheading(270)
    neo.forward(10)


def right():
    neo.setheading(0)
    neo.forward(10)
    


def left():
    neo.setheading(180)
    neo.forward(10)


# def







#color/drawing functions






#create screem
wn = trtl.Screen()



#bind to keypresses
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")

#listen
wn.listen()



#mainloop
wn.mainloop()