@echo off
setlocal

cd /d "%~dp0\.."

if not exist .venv (
    echo Creating virtual environment...
    py -3.12 -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e .[dev]
python -m fullmedia_alchemist

endlocal
