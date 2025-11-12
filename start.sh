#!/bin/bash

# Nova AI Assistant Start Script

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the assistant
python3 main.py

