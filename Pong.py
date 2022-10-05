#import library
import pygame
#initialization
pygame.init()
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = ()
RED = ()
YELLOW = ()

#Paddle width and height
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
#height, width, window
WINNING_SCORE = 10
WIDTH, HEIGHT= 600, 500
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
SCORE_FONT = pygame.font.SysFont("Arial", 50)
#Caption
pygame.display.set_caption("PONG")
#Ball Class
class Ball:
    #Class constants
    COLOR = WHITE
    #Max Velocity
    MAX_VEL = 5


    def __init__(self, x, y, radius):
        #Original_x/Original_y will save the original value after game resets.
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        #velocity will change depending on direction of contact.
        self.y_vel = 0
    
    #Draws ball
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR,(self.x, self.y), self.radius)
    #Moves ball
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    #Resets ball
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

#Paddle Class
class Paddle:
    COLOR = WHITE
    VEL = 9
    def __init__(self, x, y, height, width):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
    #Draws paddles(declare)
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR,(self.x, self.y, self.height, self.width))
    #Move method for paddles
    def move(self, up= True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

#Settings Class
#never finished
class Settings:
    def __init__(self, win, keys):
        self.win = win
        self.keys = keys
        
    #def key_get_pressed(self):
#draw function(catalyst for drawing objects)
def draw(win, paddles, ball, left_score, right_score):

    #Was not necessary
    win.fill(BLACK)
    #render text to screen
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    #draw and position text on screen
    win.blit(left_score_text,(WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text,(WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    #Draws paddles(call)
    for paddle in paddles:
        paddle.draw(win)
    #Draws dotted rects(starts at 10, ends at the bottom of the screen, steps by 500/20(25). Distances itself by 25 pixels.)
    for i in range(10, HEIGHT, HEIGHT//PADDLE_HEIGHT):
        #Continues the loop even when it crosses an odd pixel.
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE,(WIDTH//2 - 5, i, 10, HEIGHT//20))
        #Calling draw(Ball class)
        ball.draw(win)
    #Constantly refreshes screen
    pygame.display.update()
#Handling paddle movement
def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up= True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up= False)

    if keys[pygame.K_UP]and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up= True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up= False)

def collision(ball, left_paddle, right_paddle):

    if ball.y + ball.radius >= HEIGHT:
        #Handling collision with ceiling
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    #Handling collision with paddles
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel = -1 * ball.x_vel

                middle_y = left_paddle.y + left_paddle.height / 2
                diff_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = diff_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel = -1 * ball.x_vel

                middle_y = right_paddle.y + right_paddle.height / 2
                diff_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = diff_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

#Main Program
def main():
    FPS = 60
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT,PADDLE_WIDTH)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_HEIGHT, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT,PADDLE_WIDTH)
    left_score = 0
    right_score = 0
    ball = Ball(WIDTH//2, HEIGHT//2, 7)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        #Key input
        keys = pygame.key.get_pressed()

        handle_paddle_movement(keys, left_paddle, right_paddle)
        #Call ball.move method

        ball.move()
        collision(ball,left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
        #Calling draw function to draw objects for us
        draw(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)

        won = False

        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won"
        elif right_score >= WINNING_SCORE:
           won = True
           win_text = "Right Player Won"
        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WINDOW.blit(text,(WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

            pygame.display.update()
            pygame.time.delay(500)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            
    
if __name__ == '__main__':
    main()