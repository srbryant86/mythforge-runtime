# Morale system: affects unit behavior based on battlefield events
class MoraleSystem:
    def __init__(self):
        self.unit_morale = {}
    def update_morale(self, unit_id, delta):
        self.unit_morale[unit_id] = self.unit_morale.get(unit_id, 100) + delta
    def get_morale(self, unit_id):
        return self.unit_morale.get(unit_id, 100)
