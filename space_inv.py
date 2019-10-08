# Space Invaders
# import turtle and os modules
import turtle
from playsound import playsound
import math
import random

#global bulletstate
#bulletstate = "ready"
# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# set the score to zero
score = 0

# draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# choose number of enemies
number_of_enemies = 5
# create a list of enemies
enemies = []
# add enemies to the list
for i in range(number_of_enemies):
    # create enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet2 = turtle.Turtle()
bullet2.color("yellow")
bullet2.shape("triangle")
bullet2.penup()
bullet2.speed(0)
bullet2.setheading(90)
bullet2.shapesize(0.5, 0.5)
bullet2.hideturtle()


bulletspeed = 30

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"
bulletstate2 = "ready"

# move the player left and right
# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bulletstate, bulletstate2
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        playsound("laser.wav", False)
    else:
        if bulletstate2 == "ready":
            bulletstate2 = "fire"
            # Move the bullet to the just above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet2.setposition(x, y)
            bullet2.showturtle()
            playsound("laser.wav", False)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        # Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # play sound
            playsound("explosion.wav", False)
            # update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(bullet2, enemy):
            # Reset the bullet
            bullet2.hideturtle()
            bulletstate2 = "ready"
            bullet2.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # play sound
            playsound("explosion.wav", False)
            # update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    if bulletstate2 == "fire":
        y = bullet2.ycor()
        y += bulletspeed
        bullet2.sety(y)


    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if bullet2.ycor() > 275:
        bullet2.hideturtle()
        bulletstate2 = "ready"


wn.exitonclick()
