@echo off
echo Setting up Python environment for Bizlaw Site...

cd /d "C:\Users\user\Desktop\bizlaw-site"

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install required packages
echo Installing required packages...
pip install google-generativeai requests

echo Setup completed successfully!
echo Now you can run: generate_and_push.bat

pause
