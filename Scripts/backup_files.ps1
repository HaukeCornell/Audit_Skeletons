$sourcePath = 'H:/.shortcut-targets-by-id/1vC0zCgIRTolHRYTTqSAxkjZ-qE9lQ15K/Auditing Instruments'
$destinationPath = 'D:/Auditing Instruments'

Get-ChildItem -Path $sourcePath -Recurse | Where-Object {
    !$_.PSIsContainer -and
    !($_.Extension -eq '.tak') -and
    !($_.Extension -eq '.fbx')
} | ForEach-Object {
    $destinationFile = $_.FullName.Replace($sourcePath, $destinationPath)
    $destinationDirectory = [System.IO.Path]::GetDirectoryName($destinationFile)

    if (!(Test-Path -Path $destinationDirectory)) {
        New-Item -ItemType Directory -Force -Path $destinationDirectory
    }

    if (!(Test-Path -Path $destinationFile)) {
        Copy-Item -Path $_.FullName -Destination $destinationFile
        Write-Host "Copied $($_.FullName) to $destinationFile"
    }
    else {
        Write-Host "File $destinationFile already exists. Skipping."
    }
}

Write-Host "Files copied successfully."
