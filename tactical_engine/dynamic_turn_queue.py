# Dynamic Turn Queue based on unit stats
def build_turn_queue(units):
    return sorted(units, key=lambda u: u.stats.get('speed', 1), reverse=True)
