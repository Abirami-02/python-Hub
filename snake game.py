import turtle
import time
import random

delay=0.1;

#score
score=0;
high_score=0;

#set up the Screen
wn=turtle.Screen();
wn.bgcolor("green");
wn.title("Snake game by @Abii");
wn.setup(width=600, height=600);
wn.tracer(0)#this animation turn off the updates in our screen.For that we use a update()func;

#head of the Snake
head = turtle.Turtle();
head.speed(0);
head.shape("circle");
head.color("black");
head.penup();
head.goto(0,0); #goto(x cor ,y cor)it start the snake from centre of the screen
head.direction="stop"

#Snake food
food = turtle.Turtle();
food.speed(0);
food.shape("circle");
food.color("pink");
food.penup();
food.goto(0,100);

segments=[];


pen=turtle.Turtle();
pen.color("white");
pen.penup();
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 High Score:0",align="center",font=("courier",18,"normal"))
#Function

def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_right():
    if head.direction!="left":
        head.direction="right"

def go_left():
    if head.direction!="right":
        head.direction="left"
    
def move():
    if head.direction =="up":
        y=head.ycor() # y cordinate 
        head.sety(y+20)

    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction =="right": # X cordinate 
        x=head.xcor()
        head.setx(x+20)

    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20);
# Keyboard Bindings popular choice W->up,A->left,S->down,D->right / Arrow keys

wn.listen();
wn.onkeypress(go_up,"Up");
wn.onkeypress(go_down,"Down");
wn.onkeypress(go_right,"Right");
wn.onkeypress(go_left,"Left");

#Main part of the game
while True:
    wn.update();
    # check for the collision with border
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 ):
        time.sleep(1);
        head.goto(0,0);
        head.direction="stop";
     # hide the segements --- we need a head first ,we use a backward move so segement act as a head when we again start the game we need to hide the segment
        for seg in segments:
            seg.goto(1000,1000) # apart from window 600
        
     # clear the segments
        segments.clear();
     # Reset the score and delay
        score=0;
        delay=0.1;
        
     # Update the score
        pen.clear() # else it rewrite the score itself
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("courier",18,"normal"))
    # check for the collision with food
    if head.distance(food)<20:
        #Move the food  to a random place
        x=random.randint(-290,290)
        y=random.randint(-290,280)
        food.goto(x,y);
    # Add a segment
        new_segment=turtle.Turtle();
        new_segment.speed(0);
        new_segment.shape("circle");
        new_segment.color("red");
        new_segment.penup();
        segments.append(new_segment);

        # shorten the delay to improve the game speed 
        delay -=0.001;
        #Increase the score

        score+=10;
        if(score>high_score):
            high_score=score
            pen.clear() # else it rewrite the score itself
            pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("courier",18,"normal"))
        
     # move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1): #list index start with zero so find the length with -1 and the step will not be increment so set as 0;
        x= segments[index-1].xcor()
        y= segments[index-1].ycor()
        segments[index].goto(x,y); # it decrement by 9,8,7,6,5,4,3,2,1

    # Move segment 0 to where the head 
    if len(segments)>0:
        x=head.xcor();
        y=head.ycor();
        segments[0].goto(x,y)     
     
    
    move();

    # Check for head collision wid body
    for seg in segments:
        if seg.distance(head)<20:
             time.sleep(1);
             head.goto(0,0);
             head.direction="stop";
            
    time.sleep(delay);
wn.mainloop()
