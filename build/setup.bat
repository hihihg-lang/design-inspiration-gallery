@echo off
title Design Inspiration Gallery - Setup
echo ========================================
echo   Design Inspiration Gallery - Setup
echo   30 UI Design Styles Gallery
echo ========================================
echo.
echo This will install the app to your chosen location.
echo.

set /p "INSTALLDIR=Enter installation path (default: %LOCALAPPDATA%\Programs\DesignGallery): "
if "%INSTALLDIR%"=="" set "INSTALLDIR=%LOCALAPPDATA%\Programs\DesignGallery"

echo.
echo Installing to: %INSTALLDIR%
echo.

echo Copying files...
if exist "%INSTALLDIR%" rmdir /s /q "%INSTALLDIR%"
xcopy /e /i /q "%~dp0app" "%INSTALLDIR%"

echo Creating shortcuts...
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\Design Inspiration Gallery.lnk'); $s.TargetPath = '%INSTALLDIR%\index.html'; $s.IconLocation = '%INSTALLDIR%\icons\icon-192.png,0'; $s.Save()"
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut([Environment]::GetFolderPath('StartMenu') + '\Programs\Design Inspiration Gallery.lnk'); $s.TargetPath = '%INSTALLDIR%\index.html'; $s.IconLocation = '%INSTALLDIR%\icons\icon-192.png,0'; $s.Save()"

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo   Installed to: %INSTALLDIR%
echo.
echo   To uninstall, delete the folder: %INSTALLDIR%
echo.

set /p "LAUNCH=Launch now? (Y/n): "
if /i "%LAUNCH%"=="n" goto :end
start "" "%INSTALLDIR%\index.html"

:end
pause