class GameLoop:
    def __init__(self, player, map, saveFile=None,) -> None:
        self.player = player
        self.saveFile = saveFile
        self.map = map

    def update(self, events, gamestates):
        self.map.update()
        self.player.update(events)
