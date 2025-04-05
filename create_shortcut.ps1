# Get the script's directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path

# Create the shortcut
try {
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\UL Design Update Tool.lnk")
    $Shortcut.TargetPath = "pythonw.exe"
    $Shortcut.Arguments = "`"$scriptPath\automation_gui.py`""
    $Shortcut.WorkingDirectory = $scriptPath
    $Shortcut.Description = "UL Design Update Automation Tool"
    $Shortcut.Save()

    Write-Host "Shortcut created successfully on desktop: UL Design Update Tool"
} catch {
    Write-Host "Error creating shortcut: $_"
    exit 1
}
