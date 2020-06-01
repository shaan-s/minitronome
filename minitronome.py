import pygame
from playsound import playsound
pygame.init()
clock = pygame.time.Clock()
while 1:
    try:
        ms = 1000 / (60000 / int(input("What BPM would you like? ")))
        if ms > 10 or ms < 0.10:
            print("Too High / Low!")
            "" + 1
        print(ms)
        break
    except:
        print("\nInvalid!")
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("MINITRONOME")
c = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if c == 1:
        pygame.Surface.fill(win, (0,0,0))
        c = 0
    else:
        pygame.Surface.fill(win, (255,255,255))
        c = 1
    clock.tick(ms)
    playsound("metronome.wav")
    pygame.display.update()
pygame.quit()
