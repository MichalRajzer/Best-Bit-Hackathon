class GameLoop:
    def __init__(self, player, saveFile=None) -> None:
        self.player = player
        self.saveFile = saveFile

    def update(self, events):
        self.player.update(events)
