import vlc


class VLCPlayer:
    def __init__(self) -> None:
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.set_fullscreen(True)

    def play_media(self, path):
        media = self.instance.media_new(path)
        self.player.set_media(media)
        self.player.play()
        self.player.wait_until_playing()
        self.player.set_fullscreen(True)
    
