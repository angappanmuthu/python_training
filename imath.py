class imath:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def div(self):
        return self.x / self.y

    def mod(self):
        return self.x % self.y
