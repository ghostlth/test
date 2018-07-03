import pygame,random
from pygame.locals import *
from sys import exit

SCREEN_X,SCREEN_Y = 600,600

class Snake(object):
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addNode()

    def addNode(self):
        left,top = (0,0)
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,25,25)
        if self.direction == K_RIGHT:
            node.left += 25
        elif self.direction == K_LEFT:
            node.left -= 25
        elif self.direction == K_UP:
            node.top -= 25
        elif self.direction == K_DOWN:
            node.top += 25
        self.body.insert(0,node)

    def delNode(self):
        self.body.pop()

    def move(self):
        self.delNode()
        self.addNode()

    def isDead(self):
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    def changeDirection(self,dir):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,K_DOWN]
        if dir in LR and self.direction in LR:
            return
        if dir in UD and self.direction in UD:
            return
        self.direction = dir

class Food:
    def __init__(self):
        self.rect = pygame.Rect(-25,0,25,25)

    def remove(self):
        self.rect.x = -25

    def set(self):
        if self.rect.x ==-25:
            allpos = []
            for pos in range(25,SCREEN_X-25,25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)

            print(self.rect)


def main():
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size,0,32)

    score = 0
    snake = Snake()
    food = Food()

    isdead = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("Snake")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                snake.changeDirection(event.key)
                if event.key == pygame.K_SPACE and isdead:
                    return main()
            # print(event)


        if not isdead:
            snake.move()
            print(snake.body[0].x,snake.body[0].y)
        isdead = snake.isDead()
        screen.fill((255,255,255))
        for rect in snake.body:
            pygame.draw.rect(screen,(20,220,39),rect,0)

        if food.rect == snake.body[0]:
            score += 1
            food.remove()
            snake.addNode()

        food.set()
        while food.rect in snake.body:
            print("false")
            food.remove()
            food.set()


        # autoRun_simple(snake)
        group = sliceScreen(snake, food)
        # autoRun_stupid(snake, food, group)

        pygame.draw.rect(screen,(136,0,21),food.rect,0)
        screen.blit(pygame.font.SysFont("宋体",60).render(str(score),1,(223,223,223)),(50,500))

        pygame.display.update()
        clock.tick(30)

def sliceScreen(snake,food):

    group = []
    for row in range(int(SCREEN_X/25)):
        c = []
        for col in range(int(SCREEN_Y/25)):
            c.append(0)
        group.append(c)
    # print(group)

    l_snake = []
    for cell in snake.body:
        x = int(cell.x/25)
        y = int(cell.y/25)
        l_snake.append((x,y))
        group[y][x] = 1
    # print(l_snake)


    # x_food = int(food.rect.x/25)
    # y_food = int(food.rect.y/25)
    # if x_food != -1:
    #     group[y_food][x_food] = 1
    # print(x_food,y_food)

    return group

def autoRun(snake,food,group):
    s_x, s_y = int(snake.body[0].x / 25), int(snake.body[0].y / 25)
    f_x, f_y = int(food.rect.x / 25), int(food.rect.y / 25)

    print(s_x, s_y )
    print(f_x,f_y)
    for i in group:
        print(i)

    dis_l = {}
    allPath = []
    queue = []
    queue.append([(s_y,s_x)])
    # cell_list = [(queue[-1][-1][0], queue[-1][-1][1] - 1), (queue[-1][-1][0], queue[-1][-1][1] + 1),
    #              (queue[-1][-1][0] - 1, queue[-1][-1][1]), (queue[-1][-1][0] + 1, queue[-1][-1][1])]
    # while queue:
    for i in range(10):
        path = queue.pop(0)
        node = path[-1]
        if node == (f_y,f_x):
            allPath.append(path)
            print(path)
        cell_list = [(node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])]
        for cell in cell_list:
            if checkCell(group,cell) and cell not in path:
                new_path = list(path)
                new_path.append(cell)
                queue.append(new_path)
        print(node)
        print(path)
        l = (node[0]-f_x)**2 + (node[1]-f_y)**2
        dis_l[l] = path
        # print(l)
    print(dis_l)
    print(min(dis_l.keys()))
    print(dis_l[min(dis_l.keys())])
    return allPath



def checkCell(group,cell):
    if cell[0]<0 or cell[1]<0 or cell[0]>=24 or cell[1]>=24:
        # print("false")
        return False
    elif group[cell[0]][cell[1]] == 1:
        # print("false")
        return False
    elif group[cell[0]][cell[1]] == 0:
        # print("True")
        return True

def autoRun_stupid(snake,food,group):
    s_x,s_y = int(snake.body[0].x/25),int(snake.body[0].y/25)
    s_dir = snake.direction
    f_x,f_y = int(food.rect.x/25),int(food.rect.y/25)
    mov_x = s_x - f_x
    mov_y = s_y - f_y

    dir_l = checkCell(group,(s_x-1,s_y))
    dir_r = checkCell(group,(s_x+1,s_y))
    dir_d = checkCell(group, (s_x, s_y+1))
    dir_u = checkCell(group, (s_x, s_y - 1))
    if (s_dir == pygame.K_LEFT and dir_l is False) or (s_dir == pygame.K_RIGHT and dir_r is False):
        if dir_u:
            snake.changeDirection(pygame.K_UP)
        elif dir_d:
            snake.changeDirection(pygame.K_DOWN)
    elif (s_dir == pygame.K_UP and dir_u is False) or s_dir == pygame.K_DOWN and dir_d is False:
        if dir_l:
            snake.changeDirection(pygame.K_LEFT)
        elif dir_r:
            snake.changeDirection(pygame.K_RIGHT)
    if mov_x > 0:
        if dir_l:
            snake.changeDirection(pygame.K_LEFT)
        if mov_y > 0 :
            if dir_u:
                snake.changeDirection(pygame.K_UP)
            else:
                return
        elif mov_y < 0:
            if dir_d:
                snake.changeDirection(pygame.K_DOWN)
            else:
                return
        else:
            if dir_l:
                snake.changeDirection(pygame.K_LEFT)
            else:
                if dir_u:
                    snake.changeDirection(pygame.K_UP)
                elif dir_d:
                    snake.changeDirection(pygame.K_DOWN)
    elif mov_x < 0:
        if dir_r:
            snake.changeDirection(pygame.K_RIGHT)
        if mov_y > 0 :
            if dir_u:
                snake.changeDirection(pygame.K_UP)
            else:
                return
        elif mov_y < 0:
            if dir_d:
                snake.changeDirection(pygame.K_DOWN)
            else:
                return
        else:
            if dir_r:
                snake.changeDirection(pygame.K_RIGHT)
            else:
                if dir_u:
                    snake.changeDirection(pygame.K_UP)
                elif dir_d:
                    snake.changeDirection(pygame.K_DOWN)
    else:
        if mov_y > 0 :
            if dir_u:
                snake.changeDirection(pygame.K_UP)
            else:
                return
        elif mov_y < 0:
            if dir_d:
                snake.changeDirection(pygame.K_DOWN)
            else:
                return


    return

def autoRun_simple(snake):
    x,y = snake.body[0].x,snake.body[0].y
    dir = snake.direction
    LR = [pygame.K_LEFT, pygame.K_RIGHT]
    UD = [pygame.K_UP, K_DOWN]

    if dir in LR and y == 575:
        if x == 0:
            snake.changeDirection(pygame.K_UP)
            print("change up")
    elif dir in LR and y == 0:
        if x ==575:
            snake.changeDirection(pygame.K_DOWN)
    elif dir in LR and (x==575 or x==25) and y != 0:
        snake.changeDirection(pygame.K_DOWN)
        print("change down")
    if dir in UD and (y<=575):
        if y == 0:
            snake.changeDirection(pygame.K_RIGHT)
            print("change right")
        elif x != 0:
            if x < SCREEN_X/2:
                snake.changeDirection(pygame.K_RIGHT)
                print("change right")
            else:
                snake.changeDirection(pygame.K_LEFT)
                print("change left")


if __name__ == '__main__':
    # main()
    snake = Snake()
    food = Food()
    food.set()
    f_x, f_y = int(food.rect.x / 25), int(food.rect.y / 25)

    group = sliceScreen(snake,food)
    autoRun(snake, food, group)
    print(f_x, f_y)