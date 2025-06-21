# Save/Load Game State
import json
def save_game(state, filename='savegame.json'):
    with open(filename, 'w') as f:
        json.dump(state, f)
def load_game(filename='savegame.json'):
    with open(filename, 'r') as f:
        return json.load(f)
