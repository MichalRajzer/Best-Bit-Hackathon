import pygame


class Map:
    def __init__(self, file, spriteMap) -> None:
        self.file = file
        self.spriteSheet = SpriteSheet(spriteMap)
        self.map = []
        self.renderedImage = None
        self.loadMap(self.file)
        self.render()

    def loadMap(self, file):
        # map is defined as a grid of tiles
        # Each tile has a number which tells the game what it is
        # 0 = empty space
        # 1 = basic tile with top left grass
        # 2 = basic tile with top grass
        # 3 = basic tile with top right grass
        # 4 = basic tile with left grass
        # 5 = basic tile with middle grass
        # 6 = basic tile with right grass
        # 7 = basic tile with bottom left grass
        # 8 = basic tile with bottom grass
        # 9 = basic tile with bottom right grass
        tileInSpriteMap = {0: [0, 0, 32, 32], 1: [
            32, 0, 32, 32], 2: [64, 0, 32, 32], 3: [96, 0, 32, 32], 4: [32, 32, 32, 32], 5: [64, 32, 32, 32], 6: [96, 32, 32, 32], 7: [32, 64, 32, 32], 8: [64, 64, 32, 32], 9: [96, 64, 32, 32]}
        with open(file, "r") as f:
            data = f.readline().split(";")
            self.screenY = int(data[0])*32
            self.screenX = int(data[1])*32
            self.renderedImage = pygame.Surface(
                (self.screenX, self.screenY))
            for y, line in enumerate(f.readlines()):

                self.map.append([])
                for x, symbols in enumerate(line.split()):
                    if int(symbols) < 0:
                        pass
                    else:
                        print(x*32, y*32, tileInSpriteMap[int(symbols)])
                        self.map[y].append(
                            Tile(tileInSpriteMap[int(symbols)], x*32, y*32, self.spriteSheet))

    def render(self):
        for row in self.map:
            for tile in row:
                tile.draw(self.renderedImage)

    def getMap(self):
        return self.renderedImage

    def scaledToHeight(self, height):
        return pygame.transform.scale(self.renderedImage, (int(self.screenX * height/self.screenY), height))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tileType, x: int, y: int, spritesheet) -> None:
        self.tileType = tileType
        self.x = x
        self.y = y
        self.spriteSheet = spritesheet
        self.loadTexture(tileType)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def loadTexture(self, tileType):
        self.image = self.spriteSheet.getSprite(tileType)


class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((32, 32))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return sprite

    def getSprite(self, spriteData):
        x, y, width, height = spriteData
        image = self.get_sprite(x, y, 32, 32)
        return image


if __name__ == '__main__':
    pygame.init()
    # screen = pygame.display.set_mode((20*32, 4*32))
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    map = Map("game\\gameLoop\\testmap.mp", "game\\assets\\Tiles\\tilemap.png")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((80, 80, 0))
        # map.map[2][1].draw(screen)
        # screen.blit(map.spriteSheet.get_sprite(32, 0, 32, 32), (32, 0))
        mapImg = map.scaledToHeight(600)
        # mapImg = pygame.transform.scale(mapImg, (800, 600))
        screen.blit(mapImg, (0, 0))

        pygame.display.flip()
        clock.tick(60)
