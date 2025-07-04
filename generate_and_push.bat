@echo off
REM Bizlaw Site Auto Update Batch File - Fixed Version
REM Executed daily at 6:00 AM

REM Log file setup
set LOG_FILE=C:\Users\user\Desktop\bizlaw-site\update_log.txt

echo ======================================== >> %LOG_FILE%
echo Bizlaw Site Auto Update Started >> %LOG_FILE%
echo Execution Time: %date% %time% >> %LOG_FILE%
echo ======================================== >> %LOG_FILE%

echo ========================================
echo Bizlaw Site Auto Update Started
echo Execution Time: %date% %time%
echo ========================================

REM Change to working directory
cd /d "C:\Users\user\Desktop\bizlaw-site"

REM Create data directory if it doesn't exist
if not exist "data" mkdir data

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo ERROR: Git is not installed or not in PATH >> %LOG_FILE%
    goto :error
)

REM Git configuration check
echo Setting Git configuration...
echo Setting Git configuration... >> %LOG_FILE%
git config user.name "show-hey-ai"
git config user.email "automation@bizlaw-site.com"

REM Fetch latest remote state
echo Fetching latest from remote repository...
echo Fetching latest from remote repository... >> %LOG_FILE%
git fetch origin main >> %LOG_FILE% 2>&1

REM Check if GOOGLE_API_KEY is set
if "%GOOGLE_API_KEY%"=="" (
    echo ERROR: GOOGLE_API_KEY environment variable is not set
    echo ERROR: GOOGLE_API_KEY environment variable is not set >> %LOG_FILE%
    echo Please run fix\setup_api_key.bat to set the API key
    echo Please run fix\setup_api_key.bat to set the API key >> %LOG_FILE%
    goto :error
)

echo API Key is set: %GOOGLE_API_KEY:~0,10%... >> %LOG_FILE%

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating Python virtual environment...
    echo Creating Python virtual environment... >> %LOG_FILE%
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install google-generativeai requests >> %LOG_FILE% 2>&1
) else (
    REM Activate Python virtual environment
    echo Activating Python virtual environment...
    echo Activating Python virtual environment... >> %LOG_FILE%
    call venv\Scripts\activate.bat
)

REM Execute question generation script
echo Generating questions...
echo Generating questions... >> %LOG_FILE%
python scripts\generate_questions.py >> %LOG_FILE% 2>&1
if errorlevel 1 (
    echo ERROR: Question generation failed
    echo ERROR: Question generation failed >> %LOG_FILE%
    goto :error
)

REM Execute story generation script
echo Generating story...
echo Generating story... >> %LOG_FILE%
python scripts\generate_story.py >> %LOG_FILE% 2>&1
if errorlevel 1 (
    echo ERROR: Story generation failed
    echo ERROR: Story generation failed >> %LOG_FILE%
    goto :error
)

REM Execute quote generation script
echo Generating daily quote...
echo Generating daily quote... >> %LOG_FILE%
python scripts\generate_quote.py >> %LOG_FILE% 2>&1
if errorlevel 1 (
    echo ERROR: Quote generation failed
    echo ERROR: Quote generation failed >> %LOG_FILE%
    goto :error
)

REM Deactivate virtual environment
deactivate

REM Get today's date in YYYYMMDD format using PowerShell (more reliable)
for /f %%i in ('powershell -Command "Get-Date -Format yyyyMMdd"') do set TODAY_DATE=%%i

echo Today's date: %TODAY_DATE% >> %LOG_FILE%

REM Check if data files were created
if not exist "data\questions_%TODAY_DATE%.json" (
    echo ERROR: Questions file was not created
    echo ERROR: Questions file was not created >> %LOG_FILE%
    goto :error
)

if not exist "data\story_%TODAY_DATE%.json" (
    echo ERROR: Story file was not created
    echo ERROR: Story file was not created >> %LOG_FILE%
    goto :error
)

if not exist "data\quote_%TODAY_DATE%.json" (
    echo ERROR: Quote file was not created
    echo ERROR: Quote file was not created >> %LOG_FILE%
    goto :error
)

echo Generated files confirmed:
echo Generated files confirmed: >> %LOG_FILE%
echo - questions_%TODAY_DATE%.json
echo - questions_%TODAY_DATE%.json >> %LOG_FILE%
echo - story_%TODAY_DATE%.json
echo - story_%TODAY_DATE%.json >> %LOG_FILE%
echo - quote_%TODAY_DATE%.json
echo - quote_%TODAY_DATE%.json >> %LOG_FILE%

REM Add generated files to Git
echo Adding generated files to Git...
echo Adding generated files to Git... >> %LOG_FILE%
git add data\questions_%TODAY_DATE%.json >> %LOG_FILE% 2>&1
git add data\story_%TODAY_DATE%.json >> %LOG_FILE% 2>&1
git add data\quote_%TODAY_DATE%.json >> %LOG_FILE% 2>&1

REM Check if there are any staged changes
git diff --staged --quiet
if not errorlevel 1 (
    echo No changes detected, skipping commit
    echo No changes detected, skipping commit >> %LOG_FILE%
    goto :success
)

REM Commit changes
echo Committing changes...
echo Committing changes... >> %LOG_FILE%
git commit -m "Auto-generated: %TODAY_DATE% questions, story, and quote" >> %LOG_FILE% 2>&1
if errorlevel 1 (
    echo ERROR: Commit failed
    echo ERROR: Commit failed >> %LOG_FILE%
    echo Git status: >> %LOG_FILE%
    git status >> %LOG_FILE% 2>&1
    goto :error
)

REM Push to GitHub Pages
echo Pushing to GitHub Pages...
echo Pushing to GitHub Pages... >> %LOG_FILE%
git push origin main >> %LOG_FILE% 2>&1
if errorlevel 1 (
    echo ERROR: Push failed - checking authentication
    echo ERROR: Push failed - checking authentication >> %LOG_FILE%
    echo Git remote info: >> %LOG_FILE%
    git remote -v >> %LOG_FILE% 2>&1
    
    REM Try to push with authentication prompt
    echo Retrying push with authentication...
    echo Retrying push with authentication... >> %LOG_FILE%
    git push origin main
    if errorlevel 1 (
        echo ERROR: Push failed after retry
        echo ERROR: Push failed after retry >> %LOG_FILE%
        goto :error
    )
)

:success
echo ========================================
echo Auto update completed successfully
echo Completion Time: %date% %time%
echo ========================================
echo Auto update completed successfully >> %LOG_FILE%
echo Completion Time: %date% %time% >> %LOG_FILE%
echo Files uploaded: >> %LOG_FILE%
echo - questions_%TODAY_DATE%.json >> %LOG_FILE%
echo - story_%TODAY_DATE%.json >> %LOG_FILE%
echo - quote_%TODAY_DATE%.json >> %LOG_FILE%
echo ======================================== >> %LOG_FILE%
exit /b 0

:error
echo ========================================
echo Error occurred during auto update
echo Error Time: %date% %time%
echo ========================================
echo Error occurred during auto update >> %LOG_FILE%
echo Error Time: %date% %time% >> %LOG_FILE%
echo Check the log file for details: %LOG_FILE%
echo ======================================== >> %LOG_FILE%
exit /b 1
