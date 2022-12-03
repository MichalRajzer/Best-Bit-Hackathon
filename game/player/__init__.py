import pygame


class Player:
    def __init__(self, screen, spriteSheet1, spriteSheet2) -> None:
        """
        Basic player class
        screen is the screen to draw to
        spriteSheet1 is the sprite sheet for the player in discharged state
        spriteSheet2 is the sprite sheet for the player in charged state"""
        # TODO UPDATE FOR TWO CHARGED AND NOT CHARGED STATES
        self.screen = screen
        self.sprite_sheet = pygame.image.load(spriteSheet1).convert()
        self.listOfAnimations = ["default", "walk", "jump", "run", "attack"]
        self.animations = {key: None
                           for key in self.listOfAnimations}
        # [animation, current frame, direction, charged]
        self.currentAnimation = ["default", 0,  1, 0]
        self.getAllSprites()
        print(self.animations)

    def update(self, events):
        pass

    def draw(self, screen):
        pass

    def getAllSprites(self):
        for animation in self.listOfAnimations:
            self.getAnimation(animation)

    def getAnimation(self, animation):
        if animation == "default":
            frames = [[0, 0, 32, 64]]
            anim = self.parseAnimation(frames)
            self.animations["default"] = [anim, None]

    def parseAnimation(self, frames):
        leftAnim = []
        rightAnim = []
        for frame in frames:
            sprite = pygame.Surface((frame[2], frame[3]))
            sprite.blit(self.sprite_sheet, (0, 0),
                        (frame[0], frame[1], frame[2], frame[3]))
            leftAnim.append(sprite)
        return [leftAnim, rightAnim]

    # def animate(self, state):
    #     self.currentAnimation = [state, 0, self.animations[]]


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((20*32, 4*32))
    player = Player(screen, "game\\assets\\player\\player.png", "")
    player.draw(screen)
    while True:
        screen.fill((70, 0, 70))
        playerImg = player.animations["default"][1][0][0][0]
        screen.blit(playerImg, (0, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
