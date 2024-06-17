@echo off


python "brightness.py"


if %errorlevel% neq 0 (
  echo Error: Python script failed to run.
  exit /b 1
)

echo Python script execution completed.
