@echo off
cls

echo Checking if Python is installed...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

echo Launching the application...
python ./GUI/chatbot_gui.py

pause
