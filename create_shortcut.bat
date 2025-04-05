@echo off
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File "create_shortcut.ps1"
pause 