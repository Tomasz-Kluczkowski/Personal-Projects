@echo off
REM activate virtual environment
call virtual_envs\python362-64bit\Scripts\activate.bat
cls

:question
echo This will delete current build directory and all its contents.
set /p answer= Do you want to proceed (y/n)?
if /i "%answer%" == "y" goto proceed
if /i "%answer%" == "n" goto terminate
echo Incorrect input & goto question

:proceed
if exist build_64bit (
    echo Deleting build directory.
    rmdir build_64bit /s /q
)
echo Running cx_Freeze script.
start /wait python cx_setup_windows_64bit.py build -b build_64bit
if exist build_64bit (
goto success
) else (
echo Cx_Freeze build failed. Please check your cx_freeze setup file.
goto terminate
)

:success
echo Cx_Freeze build completed successfully
echo Starting Inno setup compilation.
start /wait iscc inno_setup_windows_64bit.iss /O+
if exist build_64bit/Weather_App_Win_64bit_Setup.exe (
echo Inno setup compilation successul.
) else (
echo Inno setup compilation failed. Please check your setup script.
)

:terminate
pause
deactivate
