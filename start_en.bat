@echo off
chcp 932 >nul
echo ========================================
echo Business Law Level 3 - Daily Study Site
echo ========================================
echo.

cd /d "%~dp0"
echo Current Directory: %CD%
echo.

echo Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed.
    echo Please install Python and try again.
    echo.
    pause
    exit /b 1
)

echo Starting local server...
echo.

start "Bizlaw Server" cmd /k "python -m http.server 8080"

echo Waiting for server to start...
timeout /t 3 /nobreak >nul

echo.
echo Opening site in browser...
start http://localhost:8080

echo.
echo ========================================
echo Server started successfully!
echo URL: http://localhost:8080
echo.
echo To stop the server:
echo 1. Press Ctrl+C in the server window
echo 2. Or close the server window
echo ========================================
echo.
pause