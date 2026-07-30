# Design Inspiration Gallery - Windows Setup
# Run this script as Administrator for full functionality

$ErrorActionPreference = "Stop"
$host.UI.RawUI.WindowTitle = "Design Inspiration Gallery - Setup"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Design Inspiration Gallery - Setup" -ForegroundColor White
Write-Host "  30 UI Design Styles Gallery" -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ── Choose Installation Directory ──
Write-Host "Select installation directory:" -ForegroundColor Yellow
Write-Host ""

Add-Type -AssemblyName System.Windows.Forms
$folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
$folderBrowser.Description = "Choose where to install Design Inspiration Gallery"
$folderBrowser.RootFolder = [Environment+SpecialFolder]::ProgramFiles
$folderBrowser.ShowNewFolderButton = $true

# Default: %LOCALAPPDATA%\Programs\DesignGallery
$defaultPath = "$env:LOCALAPPDATA\Programs\DesignGallery"
if (-not (Test-Path $defaultPath)) {
    New-Item -ItemType Directory -Path $defaultPath -Force | Out-Null
}
$folderBrowser.SelectedPath = $defaultPath

$result = $folderBrowser.ShowDialog()
if ($result -ne [System.Windows.Forms.DialogResult]::OK) {
    Write-Host "Setup cancelled." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

$installPath = $folderBrowser.SelectedPath + "\DesignGallery"
Write-Host ""
Write-Host "Installing to: $installPath" -ForegroundColor Green
Write-Host ""

# ── Copy Files ──
$sourcePath = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourcePath = Join-Path $sourcePath "app"

Write-Host "Copying files..." -ForegroundColor Yellow
if (Test-Path $installPath) {
    Remove-Item -Recurse -Force $installPath
}
Copy-Item -Recurse -Force $sourcePath $installPath

# ── Create Desktop Shortcut ──
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutPath = Join-Path $desktopPath "Design Inspiration Gallery.url"
$shortcutContent = @"
[InternetShortcut]
URL=file:///$installPath/index.html
IconFile=$installPath\icons\icon-192.png
IconIndex=0
"@
Set-Content -Path $shortcutPath -Value $shortcutContent -Encoding ASCII

# ── Create Start Menu Shortcut ──
$startMenuPath = [Environment]::GetFolderPath("StartMenu") + "\Programs"
$startMenuShortcut = Join-Path $startMenuPath "Design Inspiration Gallery.url"
$shortcutContent = @"
[InternetShortcut]
URL=file:///$installPath/index.html
IconFile=$installPath\icons\icon-192.png
IconIndex=0
"@
Set-Content -Path $startMenuShortcut -Value $shortcutContent -Encoding ASCII

# ── Create uninstaller ──
$uninstaller = @"
@echo off
echo Uninstalling Design Inspiration Gallery...
rmdir /s /q "$installPath"
del "$desktopPath\Design Inspiration Gallery.url" 2>nul
del "$startMenuPath\Design Inspiration Gallery.url" 2>nul
echo Done.
pause
"@
Set-Content -Path "$installPath\uninstall.bat" -Value $uninstaller -Encoding ASCII

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Installed to: $installPath" -ForegroundColor White
Write-Host "  Desktop shortcut created" -ForegroundColor White
Write-Host "  Start Menu shortcut created" -ForegroundColor White
Write-Host ""
Write-Host "  To uninstall, run: $installPath\uninstall.bat" -ForegroundColor Gray
Write-Host ""

# ── Ask to launch ──
$launch = Read-Host "Launch now? (Y/n)"
if ($launch -ne "n" -and $launch -ne "N") {
    Start-Process "file:///$installPath/index.html"
}

Read-Host "Press Enter to finish"