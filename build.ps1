$exclude = @("venv", "desafio01.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desafio01.zip" -Force