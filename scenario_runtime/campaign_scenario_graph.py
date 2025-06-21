# Campaign Scenario Graph
class ScenarioNode:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.next_nodes = []
    def add_connection(self, node):
        self.next_nodes.append(node)
def create_campaign():
    intro = ScenarioNode('intro', {'type': 'dialogue'})
    siege = ScenarioNode('siege', {'type': 'battle'})
    ruins = ScenarioNode('ruins', {'type': 'battle'})
    intro.add_connection(siege)
    siege.add_connection(ruins)
    return intro
