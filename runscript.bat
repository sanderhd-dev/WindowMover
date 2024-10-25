@echo off
:: Check if this script is running as admin
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Requesting administrative privileges...
    powershell start -verb runas "%~f0"
    exit /b
)

:: Voer je Python-script uit vanuit dezelfde map als dit .bat-bestand
python "%~dp0window.py"
