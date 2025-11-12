@echo off
REM Nova AI Assistant Start Script for Windows

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM Run the assistant
python main.py

pause

