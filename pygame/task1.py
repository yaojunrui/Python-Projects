import pygame

#initialize modules
pygame.init()

#Initializing surface
screen = pygame.display.set_mode((870, 870))

#add background image
background = pygame.image.load("conan.jpg")
screen.blit(background,(0,0))  #对齐的坐标
pygame.display.update()   #显示内容

pygame.display.set_caption('柯南帅照')

done = False

while not done:
    # 循环获取事件，监听事件状态，使用get()获取事件
    for event in pygame.event.get():
        # 判断事件类型，用户是否点了"X"关闭按钮
        # pygame.QUIT 指点击右上角窗口的"X"号
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    #或者 pygame.display.updated()
    #后者可以选定区域更新，flip更新全部
