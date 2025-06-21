# Terrain Modifiers
terrain_effects = {
    'forest': {'defense': +2, 'vision': -1},
    'hill': {'range': +1},
    'water': {'movement': -2}
}
def apply_terrain(unit, terrain):
    if terrain in terrain_effects:
        for stat, mod in terrain_effects[terrain].items():
            unit.stats[stat] += mod
