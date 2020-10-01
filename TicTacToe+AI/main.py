import pygame
from random import randint
import time

###################################  INITIALIZE PYGAME  ###################################################
pygame.init()
pygame.font.init()


##################################### GAME CLASS ##########################################################

class TicTacToe:
    def __init__(self):
        self.board = []
        self.setup()
        self.difficulty = 0

    def setup(self):
        self.board = [[0, 0, 0],  # 0 - empty space
                      [0, 0, 0],  # -1 - X
                      [0, 0, 0]]  # 1 - O
        self.current_player = -1
        self.available = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def print(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    print("0 ", end="")
                if j == -1:
                    print("-1 ", end="")
                if j == 1:
                    print("1 ", end="")
            print()

    def place(self, x, y):
        if (x, y) in self.available:
            self.board[y][x] = self.current_player
            self.current_player *= -1
            self.available.remove((x, y))
            #print("placing " + str(x) + " " + str(y))
            # draw
            if self.current_player == 1:  # x
                x1 = 170 * x + 10
                x2 = 170 * (x + 1) - 10
                y1 = 170 * y + 10
                y2 = 170 * (y + 1) - 10
                pygame.draw.line(self.table, (0, 0, 0), (x1, y1), (x2, y2), 4)
                pygame.draw.line(self.table, (0, 0, 0), (x2, y1), (x1, y2), 4)
                screen.blit(self.table, (45, 45))
                pygame.display.update()
                if self.check() == 2:
                    self.auto_place()

            else:
                x1 = 170 // 2 + 170 * x
                y1 = 170 // 2 + 170 * y
                pygame.draw.circle(self.table, (0, 0, 0), (x1, y1), 75, 2)
                screen.blit(self.table, (45, 45))
        else:
            #print("\n\ntried to place on " + str(x) + " " + str(y) + "\n\n")
            pass

    def auto_place(self):
        # print(self.difficulty)
        # print(self.current_player)
        if self.difficulty == 1:  # EASY - RANDOM PICK
            place = randint(0, len(self.available) - 1)
            time.sleep(0.5)
            self.place(*self.available[place])
        elif self.difficulty == 2:  # MEDIUM - SMARTER BUT NOT IMPOSSIBLE
            time.sleep(0.5)
            self.place(*self.find())
        elif self.difficulty == 3:  # IMPOSSIBLE - AI - MINIMAX
            # time.sleep(0.5)
            self.place(*self.aimove())
            #print("\n\n\n\n\n\n\n\n")

    # medium difficulty algorithm
    def find(self):
        # STEP1 - CHECKS IF HE CAN WIN THE GAME (checking if any of the lines or diagonals has sum = -2*current_player)
        #print("step 1")
        # checking rows ald columns
        for i in range(3):
            if self.board[0][i] + self.board[1][i] + self.board[2][i] == 2 * self.current_player:
                if self.board[0][i] == 0:
                    return (i, 0)
                if self.board[1][i] == 0:
                    return (i, 1)
                else:
                    return (2, i)
            if self.board[i][0] + self.board[i][1] + self.board[i][2] == 2 * self.current_player:
                if self.board[i][0] == 0:
                    return (0, i)
                if self.board[i][1] == 0:
                    return (1, i)
                else:
                    return (2, i)
        # checking diagonals
        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 2 * self.current_player:
            if self.board[0][0] == 0:
                return (0, 0)
            if self.board[1][1] == 0:
                return (1, 1)
            else:
                return (2, 2)
        if self.board[0][2] + self.board[1][1] + self.board[2][0] == 2 * self.current_player:
            if self.board[2][0] == 0:
                return (0, 2)
            if self.board[1][1] == 0:
                return (1, 1)
            else:
                return (2, 0)

        # STEP 2 - CHECKS IF THE PLAYER CAN WIN THE GAME (checking if any of the lines or diagonals has sum = 2*current_player)
        #print("step 2")
        # checking rows ald columns
        for i in range(3):
            if self.board[0][i] + self.board[1][i] + self.board[2][i] == -2 * self.current_player:
                if self.board[0][i] == 0:
                    time.sleep(0.5)
                    return (i, 0)
                if self.board[1][i] == 0:
                    time.sleep(0.5)
                    return (i, 1)
                else:
                    time.sleep(0.5)
                    return (i, 2)
            if self.board[i][0] + self.board[i][1] + self.board[i][2] == -2 * self.current_player:
                if self.board[i][0] == 0:
                    time.sleep(0.5)
                    return (0, i)
                elif self.board[i][1] == 0:
                    time.sleep(0.5)
                    return (1, i)
                else:
                    time.sleep(0.5)
                    return (2, i)
        # checking diagonals
        if self.board[0][0] + self.board[1][1] + self.board[2][2] == -2 * self.current_player:
            if self.board[0][0] == 0:
                time.sleep(0.5)
                return (0, 0)
            elif self.board[1][1] == 0:
                time.sleep(0.5)
                return (1, 1)
            else:
                time.sleep(0.5)
                return (2, 2)
        if self.board[0][2] + self.board[1][1] + self.board[2][0] == -2 * self.current_player:
            if self.board[2][0] == 0:
                time.sleep(0.5)
                return (0, 2)
            elif self.board[1][1] == 0:
                time.sleep(0.5)
                return (1, 1)
            else:
                time.sleep(0.5)
                return (2, 0)
        # STEP 3 - RANDOM
        #print("step 3")
        place = randint(0, len(self.available) - 1)
        time.sleep(0.5)
        return self.available[place]

    # impossible difficulty algorithm
    def aimove(self):
        best_score = float('-inf')
        best_move = None
        #print(self.board)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = 1  # AI = +1 (0)  ; PLAYER = -1 (X)
                    score = self.minimax()
                    #print("Score is " + "    " * 10, score)
                    if score > best_score:
                        best_score = score
                        best_move = (j, i)
                    self.board[i][j] = 0
        #print(best_move, best_score)
        return best_move

    def minimax(self, depth=0, Maximizing=False):  # AI is minimizing
        game_progress = self.check()
        #print("                  " + str(game_progress) + "                                  ")
        if game_progress <= 1:
            return game_progress
            # return game_progress*(10 - depth)
        #print(str(self.current_player) * 100)
        if Maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = -1
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = 0
                        best_score = min(score, best_score)
            return best_score



    def draw(self):
        screen.fill((255, 255, 255))
        self.table = pygame.Surface([510, 510], pygame.SRCALPHA, 32)
        boundaries = [0, 170, 340, 510]
        pygame.draw.line(self.table, (0, 0, 0), (boundaries[0], boundaries[1]), (boundaries[3], boundaries[1]), 4)
        pygame.draw.line(self.table, (0, 0, 0), (boundaries[0], boundaries[2]), (boundaries[3], boundaries[2]), 4)
        pygame.draw.line(self.table, (0, 0, 0), (boundaries[1], boundaries[0]), (boundaries[1], boundaries[3]), 4)
        pygame.draw.line(self.table, (0, 0, 0), (boundaries[2], boundaries[0]), (boundaries[2], boundaries[3]), 4)
        screen.blit(self.table, (45, 45))

    def check(self):
        board = self.board
        #print("checking            ", board)
        for i in range(3):
            if (board[i][0] != 0) and (board[i][0] == board[i][1] == board[i][2]):
                return board[i][0]
            elif (board[0][i] != 0) and (board[0][i] == board[1][i] == board[2][i]):
                return board[0][i]
        if (board[1][1] != 0) and ((board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2])):
            return board[1][1]

        if len(self.available) == 0:
            return 0
        available = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    available += 1
        if available == 0:
            return 0
        return 2

    def end(self, check):
        font = pygame.font.Font('freesansbold.ttf', 48)
        if check == -1:
            t = "WINNER - X"
        elif check == 1:
            t = "WINNER - O"
        else:
            t = "DRAW"
        text = font.render(t, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (display_width // 2, 600)
        screen.blit(text, textRect)
        pygame.display.update()
        global playing
        playing = False


##################################### FUNCTIONS #############################################


def check_button_hover():
    mouse = pygame.mouse.get_pos()
    for i in range(len(buttons)):
        button = buttons[i]
        if button[0][0] < mouse[0] < button[1][0] and button[0][1] < mouse[1] < button[1][1]:
            return i
    if start_button[0][0] < mouse[0] < start_button[1][0] and start_button[0][1] < mouse[1] < start_button[1][1]:
        return -2
    return -1


def press_button(b):
    for i in range(len(buttons)):
        buttons[i][2] = False
    buttons[b][2] = True


##################################### GAME VARIABLES #######################################################


display_height = 800
display_width = 600
fps = 30
running = True

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TicTacToe')
clock = pygame.time.Clock()

# buttons
color = (255, 255, 255)
# light shade of the buttons
color_light = (170, 170, 170)
# dark shade of the buttons
color_dark = (100, 100, 100)
# defining a font
buttonfont = pygame.font.SysFont('Corbel', 28)
#           coordinates          pressed     text
buttons = [[(20, 600), (145, 660), True, "vs Player"],
           [(165, 600), (290, 660), False, "Easy"],
           [(310, 600), (435, 660), False, "Medium"],
           [(455, 600), (580, 660), False, "Impossible"]]
start_button = [(165, 440), (435, 540)]
startbuttonfont = pygame.font.SysFont('Corbel', 90)
logofont = pygame.font.SysFont('Corbel', 120)
running = True
game = TicTacToe()
playing = True
game.draw()
x = -1
y = -1


def start(restart=False):
    global running
    menu_running = True
    screen.fill((255, 255, 255))
    if restart:
        startbuttontext = startbuttonfont.render("Restart", True, color)
    else:
        startbuttontext = startbuttonfont.render("Start", True, color)
    logotext = logofont.render("TicTacToe", True, color_dark)
    while menu_running:
        b = check_button_hover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                menu_running = False
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b >= 0:
                    press_button(b)
                    #print("Pressed")
                    game.difficulty = b
                elif b == -2:
                    play()
                    menu_running = False
        for button in buttons:
            if button[2]:
                pygame.draw.rect(screen, color_light, [*button[0], 125, 60])
            else:
                pygame.draw.rect(screen, color_dark, [*button[0], 125, 60])
            buttontext = buttonfont.render(button[3], True, color)
            screen.blit(buttontext, button[0])
        pygame.draw.rect(screen, color_dark, [*start_button[0], 270, 100])
        screen.blit(startbuttontext, start_button[0])
        screen.blit(logotext,(60,100))
        pygame.display.update()
        clock.tick(fps)


def play():
    time.sleep(1)
    game.draw()
    global running
    global playing
    playing = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                pygame.quit()
            elif playing:
                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if mx > 45:
                        if mx < 215:
                            x = 0
                        elif mx < 385:
                            x = 1
                        elif mx < 555:
                            x = 2
                        else:
                            x = -1
                    else:
                        x = -1
                    if my > 45:
                        if my < 215:
                            y = 0
                        elif my < 385:
                            y = 1
                        elif my < 555:
                            y = 2
                        else:
                            y = -1
                    else:
                        y = -1
                    game.place(x, y)
                    # game.print()
                    check = game.check()
                    if check < 2:
                        game.end(check)
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    game.setup()
                    start(restart=True)
            # print(event)
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    start()

