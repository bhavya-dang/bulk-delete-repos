# Read the repository list from file and delete each repository
Get-Content ./output.txt | ForEach-Object {
    Invoke-WebRequest -Uri "https://api.github.com/repos/$_" -Method "DELETE" -Headers @{
        "Authorization"="token <token>"
    }
}

# Display a success message after completion
Write-Host "All repositories have been successfully deleted!" -ForegroundColor Green
