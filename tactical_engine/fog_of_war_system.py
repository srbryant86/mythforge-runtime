# Fog of War System
class FogOfWar:
    def __init__(self, map_size):
        self.visible = [[False]*map_size[1] for _ in range(map_size[0])]
    def reveal(self, x, y, radius):
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.visible) and 0 <= ny < len(self.visible[0]):
                    self.visible[nx][ny] = True
    def is_visible(self, x, y):
        return self.visible[x][y]
