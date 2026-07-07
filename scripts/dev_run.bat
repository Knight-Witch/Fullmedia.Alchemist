@echo off
setlocal

cd /d "%~dp0\.."

echo ============================================================
echo Fullmedia Alchemist - Dev Run
echo ============================================================
echo.

where py >nul 2>nul
if errorlevel 1 (
    echo ERROR: Python launcher "py" was not found.
    echo Install Python 3.12+ or make sure the Python launcher is available.
    goto :fail
)

if not exist .venv (
    echo Creating virtual environment...
    py -3.12 -m venv .venv
    if errorlevel 1 goto :fail
)

call .venv\Scripts\activate.bat
if errorlevel 1 goto :fail

echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 goto :fail

echo Installing Fullmedia Alchemist in editable dev mode...
python -m pip install -e ".[dev]"
if errorlevel 1 goto :fail

echo.
echo Launching Fullmedia Alchemist...
echo.
python -m fullmedia_alchemist
if errorlevel 1 goto :fail

echo.
echo App exited normally.
goto :done

:fail
echo.
echo ============================================================
echo Fullmedia Alchemist failed to launch.
echo Copy the error text above and send it for debugging.
echo ============================================================
pause
exit /b 1

:done
pause
endlocal
