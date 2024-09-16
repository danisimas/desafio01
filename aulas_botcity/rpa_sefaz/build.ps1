$exclude = @("venv", "rpa_sefaz.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "rpa_sefaz.zip" -Force