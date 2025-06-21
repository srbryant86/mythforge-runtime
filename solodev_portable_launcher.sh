#!/bin/bash

# SoloDev Portable Launcher
# Description: Launches SoloDev runtime from any directory

# Resolve script path
SCRIPT_DIR="$(cd "$(dirname \"${BASH_SOURCE[0]}\")" && pwd)"
cd "$SCRIPT_DIR"

# Setup environment
export SOLODEV_ENV=production
export SOLODEV_HOME="$SCRIPT_DIR"
export PATH="$SOLODEV_HOME:$PATH"

# Log system info
echo "Launching SoloDev from: $SOLODEV_HOME"
echo "Runtime environment: $SOLODEV_ENV"
echo "Platform: $(uname -a)"

# Launch Python core
if [ -f "./run_engine.py" ]; then
    echo "Running SoloDev Engine..."
    python3 ./run_engine.py "$@"
else
    echo "Error: SoloDev engine not found at $SOLODEV_HOME/run_engine.py"
    exit 1
fi
