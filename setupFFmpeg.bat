@echo off
@setlocal enabledelayedexpansion
Title ffmpeg setup for Windows

:: Verificar si se ejecuta como administrador
NET FILE >NUL 2>&1
IF '%ERRORLEVEL%' NEQ '0' (
    echo Error: This script must be run as administrator.
    echo Please right-click on the script and select "Run as administrator".
    pause
    exit /b 1
)

:: URL para descargar la última versión de FFmpeg
set "base_url=https://github.com/BtbN/FFmpeg-Builds/releases/latest"
set "download_url=https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
set "zip_file=ffmpeg-master-latest-win64-gpl.zip"
set "install_dir=C:\ffmpeg"
set "ffmpeg_dir=%install_dir%\ffmpeg-master-latest-win64-gpl"

echo Downloading FFmpeg for Windows, please wait and do not close this window...
powershell -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%download_url%' -OutFile '%zip_file%'"

if not exist "%zip_file%" (
    echo Error: Failed to download FFmpeg. Try again. 
    pause
    exit /b 1
)

echo Unpacking FFmpeg...
if not exist "%install_dir%" (
    mkdir "%install_dir%"
)
powershell -command "Expand-Archive -Path '%zip_file%' -DestinationPath '%install_dir%' -Force"

:: Actualizar el PATH solo si no está ya incluido
echo %PATH% | find /i "%ffmpeg_dir%\bin" > nul
if errorlevel 1 (
    setx /M PATH "%PATH%;%ffmpeg_dir%\bin"
    echo PATH has been updated to include FFmpeg.
) else (
    echo PATH was already set to include FFmpeg.
)

:: Limpiar archivo ZIP
del "%zip_file%"

echo FFpeg has been installed successfully.
echo FFmpeg has been installed in : %ffmpeg_dir%
pause
exit /b 0