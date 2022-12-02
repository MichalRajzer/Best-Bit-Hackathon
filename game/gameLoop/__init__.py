class GameLoop:
    def __init__(self, player, saveFile=None) -> None:
        self.player = player
        self.saveFile = saveFile

    def update(self, events, gamestates):
        self.player.update(events)
