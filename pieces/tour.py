from pieces import piece

class tour (piece):
    def __init__(self, color, name):
        self.name = "tour"
        self.color = color
        self.position = none

    def mooves (self, position):
        #deplace la piece dans les bonnes directions en +