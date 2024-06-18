@echo off

@REM setlocal enabledelayedexpansion

@REM for /f "tokens=*" %%a in ('cd') do set scriptdir=%%a

@REM python "!scriptdir!\brightness.py"
@REM endlocal

python C:\Users\Username\Documents\brighntess\brightness.py
if %errorlevel% neq 0 (
  echo Error: Python script failed to run.
  exit /b 1
)

echo Python script execution completed.
