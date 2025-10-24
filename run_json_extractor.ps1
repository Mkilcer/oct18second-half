# PowerShell script to run JSON information extraction programs
# Date: October 18, 2025

Write-Host "=== JSON Information Extraction Tools ===" -ForegroundColor Green
Write-Host "This script will run Python programs to extract specific information from JSON files" -ForegroundColor Yellow

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
Write-Host "`nChecking for JSON files..." -ForegroundColor Cyan
if (Test-Path "sample.json") {
    Write-Host "✓ Found sample.json" -ForegroundColor Green
    $jsonContent = Get-Content "sample.json" -Raw
    Write-Host "Content preview: $jsonContent" -ForegroundColor Yellow
} else {
    Write-Host "✗ sample.json not found" -ForegroundColor Red
    Write-Host "Creating a sample JSON file..." -ForegroundColor Yellow
    $sampleData = @"
{
    "name": "mk",
    "age": "89",
    "city": "hihus",
    "email": "mk@example.com",
    "hobbies": ["reading", "coding", "music"],
    "profile": {
        "isActive": true,
        "lastLogin": "2025-10-18",
        "preferences": {
            "theme": "dark",
            "language": "en"
        }
    }
}
"@
    $sampleData | Out-File -FilePath "sample.json" -Encoding UTF8
    Write-Host "✓ Created sample.json with extended data" -ForegroundColor Green
}

Write-Host "`n" + "="*60 -ForegroundColor Yellow
Write-Host "OPTION 1: Simple JSON Extraction Example" -ForegroundColor Cyan
Write-Host "="*60 -ForegroundColor Yellow

try {
    py "simple_json_extract.py"
    Write-Host "`n✓ Simple extraction completed!" -ForegroundColor Green
} catch {
    Write-Host "✗ Error running simple extraction." -ForegroundColor Red
    Write-Host $Error[0] -ForegroundColor Red
}

Write-Host "`n" + "="*60 -ForegroundColor Yellow
Write-Host "OPTION 2: Interactive JSON Extractor" -ForegroundColor Cyan
Write-Host "="*60 -ForegroundColor Yellow
Write-Host "Starting interactive JSON extractor..." -ForegroundColor Yellow
Write-Host "(You can explore different extraction options)" -ForegroundColor Yellow

try {
    py "json_extractor.py"
    Write-Host "`n✓ Interactive extraction completed!" -ForegroundColor Green
} catch {
    Write-Host "✗ Error running interactive extractor." -ForegroundColor Red
    Write-Host $Error[0] -ForegroundColor Red
}

# Show generated files
Write-Host "`nChecking generated files..." -ForegroundColor Cyan
$generatedFiles = @("filtered_info.json", "summary_report.json")
foreach ($file in $generatedFiles) {
    if (Test-Path $file) {
        Write-Host "✓ Generated: $file" -ForegroundColor Green
        $content = Get-Content $file -Raw
        Write-Host "Content: $content" -ForegroundColor Yellow
    } else {
        Write-Host "✗ Not found: $file" -ForegroundColor Red
    }
}

Write-Host "`n" + "="*60 -ForegroundColor Green
Write-Host "JSON Extraction Tools Completed!" -ForegroundColor Green
Write-Host "="*60 -ForegroundColor Green

Write-Host "`nPress any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")