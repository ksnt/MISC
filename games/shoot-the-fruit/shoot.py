from random import randint
apple = Actor("apple")
red_ball= Actor("ball")
points = 0

def draw():
    screen.clear()
    apple.draw()
    red_ball.draw()
    screen.draw.text(str(points)+"points", topleft=(10,10))

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        #points = points + 10
        place_apple()
    else:
       print("You missed")
       #quit()

place_apple()

