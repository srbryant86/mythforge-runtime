# Status Effects System
class StatusEffect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    def tick(self):
        self.duration -= 1
        return self.duration > 0
