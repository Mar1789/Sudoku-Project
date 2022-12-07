class cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.value = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_sketched_value(self, value):
        self.sketched_value = value