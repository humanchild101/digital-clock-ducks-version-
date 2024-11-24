import pygame
import random
S_WIDTH, S_HEIGHT = 1000,1000
class Duck:
    def __init__(self, duck_type, left_frames, right_frames, command = None, command2 = None):
        self.x_pos = random.randint(50, S_WIDTH-50) #random position on screen
        self.y_pos = random.randint(50, S_HEIGHT-50)
        self.velx = random.choice([random.randint(-50, -1), random.randint(1, 50)])/100 #random speed of movement
        self.vely = random.choice([random.randint(-50, -1), random.randint(1, 50)])/100 #random speed of movement

        self.left_frames = left_frames #left + right animations
        self.right_frames = right_frames

        self.direction = random.choice(["left", "right"])

        self.frame = 0 #current frame
        self.anim_cool = 60 #every 70 milliseconds frame changes

        self.duck_type = duck_type #cute or insane
        self.calmed = False  #if clicked/patted they will stop moving

        self.last_update = pygame.time.get_ticks()

        self.duck_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Transparent surface
        self.duck_surface.fill((0, 0, 0, 0))

        self.cuteclicks = 0
        self.insaneclicks = 0

        self.command = command
        self.command2 = command2

    def move(self, surface):
        current_time = pygame.time.get_ticks()

        self.x_pos += self.velx
        self.y_pos += self.vely

        if self.x_pos > S_WIDTH or self.x_pos < 0:
            self.velx *= -1
        if self.y_pos > S_HEIGHT or self.y_pos < 0:
            self.vely *= -1

        # Update animation frame
        if current_time - self.last_update >= self.anim_cool:
            self.frame = (self.frame + 1) % len(self.right_frames)
            self.last_update = current_time

        self.duck_surface.fill((0, 0, 0, 0))


        # Draw the new frame
        if self.velx > 0:
            surface.blit(self.right_frames[self.frame], (self.x_pos, self.y_pos))
        if self.velx < 0:
            surface.blit(self.left_frames[self.frame], (self.x_pos, self.y_pos))

        surface.blit(self.duck_surface, (self.x_pos, self.y_pos))

    def clicked(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.duck_type == "cute":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] >= self.x_pos and mouse_pos[0] <= self.x_pos + 183 and mouse_pos[1] >= self.y_pos and mouse_pos[1] <= self.y_pos + 161:
                    if self.command != None:
                       self.command()
                    if self.command2 != None:
                        self.command2()
                    self.cuteclicks += 1
                    if self.cuteclicks >= 1:
                        self.calmed = True
                        self.velx = 0
                        self.vely = 0
                        self.anim_cool = 100000000

        if self.duck_type == "insane":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] >= self.x_pos and mouse_pos[0] <= self.x_pos + 190 and mouse_pos[1] >= self.y_pos and mouse_pos[1] <= self.y_pos + 195:
                    if self.command != None:
                        self.command()
                    if self.command2 != None:
                        self.command2()
                    self.insaneclicks += 1
                    if self.insaneclicks >= random.choice([2,3]):
                        self.calmed = True
                        self.velx = 0
                        self.vely = 0
                        self.anim_cool = 1000000







'''
        def move(self, surface):
            current_time = pygame.time.get_ticks()

            self.x_pos += self.velx
            self.y_pos += self.vely

            if self.x_pos > S_WIDTH or self.x_pos < 0:
                self.velx *= -1
            if self.y_pos > S_HEIGHT or self.y_pos < 0:
                self.vely *= -1

            # Update animation frame
            if current_time - self.last_update >= self.anim_cool:
                self.frame = (self.frame + 1) % len(self.right_frames)
                self.last_update = current_time

            self.duck_surface.fill((0, 0, 0, 0))


            # Draw the new frame
            if self.velx > 0:
                surface.blit(self.right_frames[self.frame], (self.x_pos, self.y_pos))
            else:
                surface.blit(self.left_frames[self.frame], (self.x_pos, self.y_pos))

            surface.blit(self.duck_surface, (self.x_pos, self.y_pos))

    '''