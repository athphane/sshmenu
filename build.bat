@echo off

REM Activate the virtual environment
call .\venv\Scripts\activate.bat

REM Run PyInstaller to compile the script
call pyinstaller -n sshmenu --onefile main.py

REM Pause the script to keep the console window open
pause
