# PowerShell Script to Create GitHub Release
# Author: RSK World | Website: https://rskworld.in
# Usage: .\create_release.ps1 -Version "v1.0.0" -Token "your_github_token"

param(
    [Parameter(Mandatory=$true)]
    [string]$Version,
    
    [Parameter(Mandatory=$true)]
    [string]$Token,
    
    [string]$Repo = "rskworld/pandas-guide",
    [string]$IsPrerelease = "false"
)

$headers = @{
    "Authorization" = "token $Token"
    "Accept" = "application/vnd.github.v3+json"
}

$releaseNotes = Get-Content "RELEASE_NOTES.md" -Raw

$body = @{
    tag_name = $Version
    name = "Pandas Data Manipulation Guide $Version"
    body = $releaseNotes
    draft = $false
    prerelease = ($IsPrerelease -eq "true")
} | ConvertTo-Json

$uri = "https://api.github.com/repos/$Repo/releases"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -ContentType "application/json"
    Write-Host "Release created successfully!" -ForegroundColor Green
    Write-Host "Release URL: $($response.html_url)" -ForegroundColor Cyan
} catch {
    Write-Host "Error creating release: $_" -ForegroundColor Red
    Write-Host "Response: $($_.Exception.Response)" -ForegroundColor Red
}

