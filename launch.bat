@echo off
cls

echo Checking if Python is installed...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

echo Checking for required Python packages...
for %%p in (openai google-generativeai gradio chromadb llama_index) do (
    echo Checking for %%p...
    python -c "import %%p" >nul 2>&1
    if errorlevel 1 (
        echo %%p is not installed.
        set /p choice="Do you want to install %%p? (y/n) "
        if /i "%choice%"=="y" (
            echo Installing %%p...
            pip install %%p
        )
    )
)

echo Launching the application...
python ./GUI/chatbot_gui.py

pause