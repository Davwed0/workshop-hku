@echo off
REM Setup script for Python Workshop (Windows)
REM This script helps you set up the workshop environment quickly

echo ==========================================
echo Python Workshop Setup Script (Windows)
echo ==========================================
echo.

REM Check Python version
echo Checking Python version...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)
echo [OK] Python is installed
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo [OK] Virtual environment created
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Could not activate virtual environment.
    echo Please run manually: venv\Scripts\activate.bat
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Install requirements
echo Installing required packages...
echo This may take a few minutes...
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo ERROR: Package installation failed.
    echo Try running: pip install -r requirements.txt
    pause
    exit /b 1
)
echo [OK] Packages installed successfully
echo.

REM Run tests
echo Running validation tests...
python test_notebooks.py

if errorlevel 1 (
    echo.
    echo WARNING: Some tests failed. Please check the errors above.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo To start the workshop:
echo   1. Make sure virtual environment is activated
echo   2. Run: jupyter notebook
echo   3. Open notebooks/01_basics.ipynb
echo.
echo Have fun learning! 🚀
echo.
pause
