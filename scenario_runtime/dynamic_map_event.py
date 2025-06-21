# Dynamic Map Event Trigger
def check_triggers(state):
    if state.get('fort_captured'):
        return 'reinforcements_arrive'
    return None
