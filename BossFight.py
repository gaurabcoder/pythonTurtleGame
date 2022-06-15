################-Import-################
import turtle as trtl
import random as rand
##############-Variables-###############
#Screen
wn = trtl.Screen()
wn.setup(width = 600, height = 600)
difficulty = wn.textinput("Difficulty Setting", "What difficuly do you want? Type 'e' for easy, 'm' for medium, and 'h' for hard.")
if difficulty == "e":
  difficulty_number = 1
if difficulty == "m":
  difficulty_number = 2
if difficulty == "h":
  difficulty_number = 4
username = wn.textinput("Username", "Type in a Username: ")
while(len(username) > 10):
  username = wn.textinput("Username", "That Username was longer than 10 characters. Type in a new Username: ")
#Loading images
wn.bgpic("BG_pic.gif")
player_shape = "Player_2.gif"
boss_shape = "The_Boss.gif"
you_won_img = "You_Won.gif"
you_lost_img = "You_Lost.gif"
title_img = "Title.gif"
#The bullets
bullet_1 = trtl.Turtle()
bullet_2 = trtl.Turtle()
bullet_3 = trtl.Turtle()
bullets = [bullet_1, bullet_2, bullet_3]
boss_bullet_1 = trtl.Turtle()
boss_bullet_2 = trtl.Turtle()
boss_bullet_3 = trtl.Turtle()
boss_bullets = [boss_bullet_1, boss_bullet_2, boss_bullet_3]
#Game variables
health_icon = "-" #What symbol the health will look like
firing = False
boss_firing = False
game_end = False
bullet_range = 90
bullets_fired = 0
##############-Initialize-###############
#Adding the images to the screen
wn.addshape(player_shape)
wn.addshape(boss_shape)
wn.addshape(you_won_img)
wn.addshape(you_lost_img)
wn.addshape(title_img)
#Title Turtle
title = trtl.Turtle()
title.shape(title_img)
title.penup()
title.goto(0, 100)
#Start Turtle
start_game_turtle = trtl.Turtle()
start_game_turtle.color("deeppink")
start_game_turtle.penup()
start_game_turtle.goto(0, 10)
instructions = ["There appears to be a Boss in front of You.",
"You will need to defeat him.",
"You have one ability:", "When you shoot, the boss and his bullets freeze.",
"Use A to move left.",
"Use D to move right.",
"Use W to shoot.", "Good Luck!!!!"]
for text in instructions:
  start_game_turtle.write(text, align = "center", font = ("Arial", 17, "bold"))
  start_game_turtle.goto(0, start_game_turtle.ycor()-20)
start_game_turtle.goto(-30, -225)
start_game_turtle.color("lightgreen")
start_game_turtle.write("Start", align = "center", font = ("Arial", 40, "normal"))
start_game_turtle.shape("triangle")
start_game_turtle.turtlesize(3)
start_game_turtle.goto(80 ,-200)
start_game_turtle.speed(2)
#Player Turtle
player = trtl.Turtle()
player.penup()
player.hideturtle()
player.goto(0, -150)
player.shape(player_shape)
player.turtlesize(.5)
#Boss Turtle
boss = trtl.Turtle()
boss.penup()
boss.hideturtle()
boss.speed(2)
boss.goto(0, 150)
boss.shape(boss_shape)
boss.shapesize(5)
#Boss Health Writer
boss_hp_writer = trtl.Turtle()
boss_hp_writer.hideturtle()
boss_hp_writer.color("red")
boss_hp_writer.penup()
boss_hp_writer.goto(0, 200)
#Player Health Writer
player_hp_writer = trtl.Turtle()
player_hp_writer.hideturtle()
player_hp_writer.color("lightgreen")
player_hp_writer.penup()
player_hp_writer.goto(0, -300)
#You Won Turtle
you_won = trtl.Turtle()
you_won.hideturtle()
you_won.shape(you_won_img)
#You Lost Turtle
you_lost = trtl.Turtle()
you_lost.hideturtle()
you_lost.shape(you_lost_img)
#Bullets Fired Turtle
bullets_fired_turtle = trtl.Turtle()
bullets_fired_turtle.hideturtle()
bullets_fired_turtle.penup()
bullets_fired_turtle.goto(0, -30)
##############-Functions-###############
#START GAME
def start_game(x,y):
  global difficulty_number
  global boss
  global player
  global title
  global start_game_turtle
  global player_health
  global boss_health
  global player_hp_writer
  global boss_hp_writer
  global health_icon
  boss_health = 8 + difficulty_number*2
  player_health = 6 - difficulty_number
  if difficulty_number == 1:
    boss_health = 7
  start_game_turtle.hideturtle()
  start_game_turtle.clear()
  title.hideturtle()
  player_hp_writer.write(health_icon*player_health, align = "center", font = ("Arial", 90, "normal"))
  boss_hp_writer.write(health_icon*boss_health, align = "center", font = ("Arial", 90, "normal"))
  player.showturtle()
  boss.showturtle()
  boss_move()
#PLAYER MOVEMENT
def move_left():
  global player
  player.goto(player.xcor() - 7, -150)
def move_right():
  global player
  player.goto(player.xcor() + 7, -150)
#PLAYER BULLET
def bullet():
  global player
  global bullets
  global firing
  global bullet_range
  global boss_health
  global boss
  global boss_hp_writer
  global game_end
  global bullets_fired
  global health_icon
  if(firing != True and game_end != True):
    bullets_fired += 1
    bullet = rand.choice(bullets)
    bullet.hideturtle()
    bullet.speed(0)
    bullet.penup()
    bullet.color("light green")
    bullet.shape("classic")
    bullet.turtlesize(1)
    bullet.goto(player.pos())
    bullet.setheading(player.heading() + 90)
    bullet.showturtle()
    firing = True
    for x in range(bullet_range):
      bullet.forward(5)
      distance = (((bullet.xcor()-boss.xcor())**2) + ((bullet.ycor()-boss.ycor())**2))**0.5
      if distance <= 30:
        bullet.turtlesize(2)
        bullet.color("orange")
        bullet.shape("circle")
        boss_health -= 1
        boss_hp_writer.clear()
        boss_hp_writer.write(health_icon*boss_health, align = "center", font = ("Arial", 90, "normal"))
        break
    bullet.hideturtle()
    firing = False
#BOSS BULLET
def boss_bullet():
  global boss
  global boss_bullets
  global boss_firing
  global bullet_range
  global player_health
  global health_icon
  global difficulty_number
  if(boss_firing != True):
    boss_bullet = rand.choice(boss_bullets)
    boss_bullet.hideturtle()
    boss_bullet.speed(0)
    boss_bullet.penup()
    boss_bullet.turtlesize(.2 + (difficulty_number / 2.5))
    boss_bullet.shape("circle")
    boss_bullet.color("red")
    boss_bullet.goto(boss.pos())
    boss_bullet.setheading(boss.heading() - 90)
    boss_bullet.showturtle()
    boss_firing = True
    boss_bullet.speed(5)
    for x in range(bullet_range):
      boss_bullet.forward(5)
      distance = (((boss_bullet.xcor()-player.xcor())**2) + ((boss_bullet.ycor()-player.ycor())**2))**0.5
      if distance <= 20 + difficulty_number*2:
        player_health -= 1
        player_hp_writer.clear()
        player_hp_writer.write(health_icon*player_health, align = "center", font = ("Arial", 90, "normal"))
        break
    boss_bullet.hideturtle()
    boss_firing = False
#BOSS MOVEMENT
def boss_move():
  global boss
  global boss_health
  global you_won
  global player_health
  global game_end
  global bullets_fired_turtle
  global bullets_fired
  if (boss_health > 0 and player_health > 0):
    boss_bullet()
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(100,200)
    boss.goto(new_xpos, new_ypos)
    boss_move()
  elif(player_health <= 0):
    you_lose()
  else: #YOU WIN
    boss.hideturtle()
    you_won.showturtle()
    game_end = True #STOPS PLAYER FROM SHOOTING AFTER GAME HAS ENDED
    boss.hideturtle()
    boss.goto(0, 50)
    bullets_fired_turtle.color("lightgreen")
    bullets_fired_turtle.write("You Fired: " + str(bullets_fired) + " Bullets", align = "center",font = ("Arial", 15, "bold"))
    drawing_win()
def drawing_win():
  global username
  yw_draw = trtl.Turtle() 
  yw_draw.color("darkgoldenrod1")
  yw_draw.speed(7)
  yw_draw.pensize(5)
  yw_draw.penup()
  yw_draw.goto(-50,240)
  yw_draw.pendown()
  yw_draw.begin_fill()
  yw_draw.forward(100)
  yw_draw.right(90)
  for x in range(12):
    yw_draw.forward(10)
    yw_draw.right(3)
  yw_draw.setheading(270)
  yw_draw.forward(60)
  yw_draw.left(90)
  yw_draw.forward(25)
  yw_draw.right(90)
  yw_draw.forward(13)
  yw_draw.right(90)
  yw_draw.forward(80)
  yw_draw.right(90)
  yw_draw.forward(13)
  yw_draw.right(90)
  yw_draw.forward(25)
  yw_draw.left(90)
  yw_draw.forward(60)
  yw_draw.left(35)
  for x in range(12):
    yw_draw.forward(10)
    yw_draw.right(3)
  yw_draw.end_fill()
  yw_draw.penup()
  yw_draw.goto(0, 200)
  yw_draw.color("green")
  yw_draw.write("Winner:", align = "center", font = ("Arial", 20, "bold"))
  yw_draw.goto(0, 175)
  yw_draw.color("darkslategray")
  yw_draw.write(username, align = "center", font = ("Arial", 13, "normal"))
  yw_draw.hideturtle()
  

#YOU LOSE
def you_lose():
  global game_end
  global player
  global you_lost
  global bullets_fired_turtle
  global bullets_fired
  game_end = True #STOPS PLAYER FROM SHOOTING AFTER GAME HAS ENDED
  you_lost.showturtle()
  player.hideturtle()
  bullets_fired_turtle.color("brown1")
  bullets_fired_turtle.write("You Fired: " + str(bullets_fired) + " Bullets", align = "center",font = ("Arial", 15, "bold"))
  drawing_lose()
def drawing_lose():
  yl_draw = trtl.Turtle()
  yl_colors = ["yellow", "orange", "red"]
  yl_draw.color(yl_colors.pop())
  yl_draw.speed(9)
  yl_draw.pensize(3)
  yl_draw.penup()
  yl_draw.goto(50,-105)
  yl_draw.pendown()
  yl_draw.begin_fill()
  for x in range(12):
    yl_draw.forward(40)
    yl_draw.right(135)
    yl_draw.forward(40)
    yl_draw.left(105)
  yl_draw.end_fill()
  yl_draw.penup()
  yl_draw.goto(33, -120)
  yl_draw.color(yl_colors.pop())
  yl_draw.pendown()
  yl_draw.begin_fill()
  for x in range(12):
    yl_draw.forward(25)
    yl_draw.right(135)
    yl_draw.forward(25)
    yl_draw.left(105)
  yl_draw.end_fill()
  yl_draw.penup()
  yl_draw.goto(15, -130)
  yl_draw.color(yl_colors.pop())
  yl_draw.pendown()
  yl_draw.begin_fill()
  for x in range(12):
    yl_draw.forward(10)
    yl_draw.right(135)
    yl_draw.forward(10)
    yl_draw.left(105)
  yl_draw.end_fill()
  yl_draw.hideturtle()

##############-Events-###############
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")
wn.onkey(bullet, "w")
wn.listen()
while(start_game_turtle.isvisible()):
  start_game_turtle.goto(start_game_turtle.xcor() - 15, -200)
  start_game_turtle.onclick(start_game)
  start_game_turtle.goto(start_game_turtle.xcor() + 15, -200)

wn.mainloop()