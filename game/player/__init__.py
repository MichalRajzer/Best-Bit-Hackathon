import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, spriteSheet, map) -> None:
        """
        Basic player class
        screen is the screen to draw to
        spriteSheet1 is the sprite sheet for the player"""
        self.map = map
        self.screen = screen
        self.state = "idle"
        self.sprite_sheet = pygame.image.load(spriteSheet).convert_alpha()
        self.listOfAnimations = ["default", "walk",
                                 "jump", "run", "attack", "death"]
        self.animations = {key: None
                           for key in self.listOfAnimations}
        # [animation, current frame, direction, charged, frames per frame]
        self.currentAnimation = ["walk", 0,  1, 0, 10]
        self.getAllSprites()
        # print(self.animations)
        self.x = self.screen.get_width() / 2
        self.y = self.screen.get_height() / 2
        self.mapX = map.respawnPoint[0] + self.x
        self.mapY = map.respawnPoint[1] + self.y
        self.physicsX = map.respawnPoint[0]
        self.physicsY = map.respawnPoint[1]
        self.frameCounter = 0
        self.events = []
        self.Vy = 0
        self.Vx = 0
        self.rect = pygame.Rect(self.physicsX+32, self.physicsY+32, 64, 64)

    def gravity(self, delta):
        #self.Vy += 1000*delta
        pass

    def calculatePosition(self, delta):
        self.mapY -= self.Vy * delta
        self.mapX -= self.Vx * delta
        self.physicsY -= self.Vy * delta
        self.physicsX -= self.Vx * delta

        self.rect = pygame.Rect(-self.physicsX, -self.physicsY, 64, 64)
        collisions = pygame.sprite.spritecollide(
            self, self.map.colliders, False)
        if collisions:
            print("collision")

    def update(self):
        """Updates the player, BUT DOESN'T UPDATE THE SCREEN"""
        self.frameCounter += 1
        if self.frameCounter == self.currentAnimation[4]:
            self.frameCounter = 0
            self.currentAnimation[1] += 1
            print(len(self.animations[self.currentAnimation[0]][0][0]))
            if self.currentAnimation[1] >= len(self.animations[self.currentAnimation[0]][0][0]):
                if self.currentAnimation[0] == "attack":
                    self.currentAnimation[0] = "default"
                    self.currentAnimation[1] = 0
                elif self.currentAnimation[0] == "death":
                    self.currentAnimation[1] = self.currentAnimation[1]-1
                else:
                    self.currentAnimation[1] = 0
        self.screen.blit(
            pygame.transform.scale(self.animations[self.currentAnimation[0]][self.currentAnimation[2]][self.currentAnimation[3]][self.currentAnimation[1]], (64, 64)), (self.x, self.y))
        #
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        for tile in self.map.colliders:
            pygame.draw.rect(self.screen, (0, 255, 0), tile.rect)
        #
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.currentAnimation[0] != "jump":
                    self.currentAnimation = [
                        "jump", 0,  self.currentAnimation[2], 0, 5]
                elif event.key == pygame.K_a and self.currentAnimation[0] != "walk":
                    print("walk")
                    self.currentAnimation = ["walk", 0, 0, 0, 10]
                    self.Vx = -100
                    self.currentAnimation[1] = 0
                elif event.key == pygame.K_d and self.currentAnimation[0] != "walk":
                    self.currentAnimation = ["walk", 0, 1, 0, 10]
                    self.Vx = 100
                    self.currentAnimation[1] = 0
                elif event.key == pygame.K_f and self.currentAnimation[0] != "death":
                    self.currentAnimation = [
                        "death", 0, self.currentAnimation[2], 0, 20]
                    self.currentAnimation[1] = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.currentAnimation = ["attack", 0,
                                         self.currentAnimation[2], 0, 10]
            elif event.type == pygame.KEYUP:
                if self.currentAnimation[0] == "walk":
                    self.Vx = 0
                    print("idle")
                    self.frameCounter = 0
                    self.currentAnimation = ["default",
                                             0, self.currentAnimation[2], 0, 1]
        self.gravity(1/60)
        self.calculatePosition(1/60)
        self.events = []

    def handleEvent(self, event):
        self.events.append(event)
        # print(event)

    def getAllSprites(self):
        for animation in self.listOfAnimations:
            self.getAnimation(animation)

    def getAnimation(self, animation):
        if animation == "default":
            frames = [[0, 32, 32]]
            anim = self.parseAnimation(frames)
            self.animations["default"] = anim
        elif animation == "walk":
            frames = [[0, 32, 32], [64, 32, 32],
                      [128, 32, 32], [192, 32, 32]]
            anim = self.parseAnimation(frames)
            self.animations["walk"] = anim

        elif animation == "jump":
            frames = [[320, 32, 32],
                      [384, 32, 32], [448, 32, 32],
                      [512, 32, 32], [576, 32, 32],
                      [640, 32, 32]]
            anim = self.parseAnimation(frames)
            self.animations["jump"] = anim
        elif animation == "run":
            frames = [[704, 32, 32], [768, 32, 32],
                      [832, 32, 32], [896, 32, 32], ]
            anim = self.parseAnimation(frames)
            self.animations["run"] = anim
        elif animation == "attack":
            frames = [[1024, 34, 32], [1088, 34, 32],]
            anim = self.parseAnimation(frames)
            self.animations["attack"] = anim
        elif animation == "death":
            frames = [[1152, 32, 32], [1216, 32, 32], [1280, 32, 32],]
            anim = self.parseAnimation(frames)
            self.animations["death"] = anim

    def parseAnimation(self, frames):
        leftAnimNotCharged = []
        leftAnimCharged = []
        rightAnimNotCharged = []
        rightAnimCharged = []
        for frame in frames:
            sprite = pygame.Surface(
                (frame[1], frame[2]), pygame.SRCALPHA, 32).convert_alpha()
            sprite.blit(self.sprite_sheet, (0, 0),
                        (frame[0], 0, frame[1], frame[2]))
            sprite.convert_alpha()
            leftAnimNotCharged.append(sprite)
        for frame in frames:
            sprite = pygame.Surface(
                (frame[1], frame[2]), pygame.SRCALPHA, 32).convert_alpha()
            sprite.blit(self.sprite_sheet, (0, 0),
                        (frame[0], 32, frame[1], frame[2]))
            sprite.convert_alpha()
            leftAnimCharged.append(sprite)
        for frame in frames:
            sprite = pygame.Surface(
                (frame[1], frame[2]), pygame.SRCALPHA, 32).convert_alpha()
            sprite.blit(self.sprite_sheet, (0, 0),
                        (frame[0], 64, frame[1], frame[2]))
            sprite.convert_alpha()
            rightAnimNotCharged.append(sprite)
        for frame in frames:
            sprite = pygame.Surface(
                (frame[1], frame[2]), pygame.SRCALPHA, 32).convert_alpha()
            sprite.blit(self.sprite_sheet, (0, 0),
                        (frame[0], 96, frame[1], frame[2]))
            sprite.convert_alpha()
            rightAnimCharged.append(sprite)
        return [[leftAnimNotCharged, leftAnimCharged], [rightAnimNotCharged, rightAnimCharged]]


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((20*32, 4*64))
    player = Player(screen, "game\\assets\\player\\player.png", "")
    # player.draw(screen)
    i = 0
    clock = pygame.time.Clock()
    # animation = ["default", 1]
    # animation = ["walk", 4]
    # animation = ["jump", 6]
    # animation = ["run", 4]
    # animation = ["attack", 2]
    animation = ["death", 3]
    while True:
        screen.fill((70, 0, 70))
        #playerImg1 = player.animations[animation[0]][0][0][i]
        #playerImg2 = player.animations[animation[0]][1][0][i]
        #playerImg3 = player.animations[animation[0]][0][1][i]
        #playerImg4 = player.animations[animation[0]][1][1][i]
        #playerImg1 = pygame.transform.scale(playerImg1, (64, 64))
        #playerImg2 = pygame.transform.scale(playerImg2, (64, 64))
        #playerImg3 = pygame.transform.scale(playerImg3, (64, 64))
        #playerImg4 = pygame.transform.scale(playerImg4, (64, 64))
        #screen.blit(playerImg1, (0, 0))
        #screen.blit(playerImg2, (0, 64))
        #screen.blit(playerImg3, (0, 128))
        #screen.blit(playerImg4, (0, 192))
        #i += 1
        # if i == animation[1]:
        #    i = 0
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                player.handleEvent(event)

        player.update()
        pygame.display.flip()
