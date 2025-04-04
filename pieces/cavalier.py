from pieces import piece

class cavalier (piece):
    def __init__(self, color, name):
        self.name = "cavalier"
        self.color = color
        self.position = none

    def mooves (self, position):
        #deplace la piece dans les bonnes directions en L de toute diretion
