# PowerShell script to run the Age Extraction tool
# Date: October 18, 2025

Write-Host "=== Age Extraction Tool ===" -ForegroundColor Green
Write-Host "This script will run a Python program that asks for user input and extracts age information from JSON" -ForegroundColor Yellow

# Check if Python is available
Write-Host "`nChecking Python installation..." -ForegroundColor Cyan
try {
    $pythonVersion = py --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Python not found. Please install Python first." -ForegroundColor Red
    exit 1
}

# Check if sample.json exists
Write-Host "`nChecking for JSON data file..." -ForegroundColor Cyan
if (Test-Path "sample.json") {
    Write-Host "✓ Found sample.json" -ForegroundColor Green
    $jsonContent = Get-Content "sample.json" -Raw
    Write-Host "Current data: $jsonContent" -ForegroundColor Yellow
} else {
    Write-Host "✗ sample.json not found" -ForegroundColor Red
    Write-Host "Creating sample.json with test data..." -ForegroundColor Yellow
    
    $sampleData = @"
{
    "name": "mk",
    "age": "89",
    "city": "hihus"
}
"@
    $sampleData | Out-File -FilePath "sample.json" -Encoding UTF8
    Write-Host "✓ Created sample.json" -ForegroundColor Green
}

Write-Host "`n" + "="*60 -ForegroundColor Yellow
Write-Host "OPTION 1: Simple Age Extractor (Recommended)" -ForegroundColor Cyan
Write-Host "="*60 -ForegroundColor Yellow
Write-Host "This will ask you for a person's name and extract their age" -ForegroundColor Yellow

$choice = Read-Host "`nRun Simple Age Extractor? (y/n)"
if ($choice -eq 'y' -or $choice -eq 'Y') {
    try {
        py "simple_age_extractor.py"
        Write-Host "`n✓ Simple age extraction completed!" -ForegroundColor Green
    } catch {
        Write-Host "✗ Error running simple age extractor." -ForegroundColor Red
        Write-Host $Error[0] -ForegroundColor Red
    }
}

Write-Host "`n" + "="*60 -ForegroundColor Yellow
Write-Host "OPTION 2: Interactive Age Extractor (Advanced)" -ForegroundColor Cyan
Write-Host "="*60 -ForegroundColor Yellow
Write-Host "This provides more detailed options and analysis" -ForegroundColor Yellow

$choice2 = Read-Host "`nRun Interactive Age Extractor? (y/n)"
if ($choice2 -eq 'y' -or $choice2 -eq 'Y') {
    try {
        py "interactive_age_extractor.py"
        Write-Host "`n✓ Interactive age extraction completed!" -ForegroundColor Green
    } catch {
        Write-Host "✗ Error running interactive age extractor." -ForegroundColor Red
        Write-Host $Error[0] -ForegroundColor Red
    }
}

# Show any generated files
Write-Host "`nChecking for generated files..." -ForegroundColor Cyan
$generatedFiles = @("extracted_age.json", "extracted_info.json")
foreach ($file in $generatedFiles) {
    if (Test-Path $file) {
        Write-Host "✓ Generated: $file" -ForegroundColor Green
        $content = Get-Content $file -Raw
        Write-Host "Content preview: $($content.Substring(0, [Math]::Min(100, $content.Length)))..." -ForegroundColor Yellow
    }
}

Write-Host "`n" + "="*60 -ForegroundColor Green
Write-Host "Age Extraction Tools Completed!" -ForegroundColor Green
Write-Host "="*60 -ForegroundColor Green

Write-Host "`nSummary of what was demonstrated:" -ForegroundColor Cyan
Write-Host "- User input collection for person's name" -ForegroundColor White
Write-Host "- JSON file loading and parsing" -ForegroundColor White
Write-Host "- Age extraction by name search" -ForegroundColor White
Write-Host "- Fallback to any available age" -ForegroundColor White
Write-Host "- Age analysis (numeric conversion, categorization)" -ForegroundColor White
Write-Host "- Interactive retry functionality" -ForegroundColor White

Write-Host "`nPress any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")