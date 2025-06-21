# Runtime bridge handler between CLI and runtime system
import subprocess
import json

def trigger_agent(agent_name):
    with open("agent_trigger_map.json") as f:
        triggers = json.load(f)
    command = triggers.get(agent_name)
    if command:
        subprocess.run(command, shell=True)
    else:
        print(f"No trigger found for agent: {agent_name}")
