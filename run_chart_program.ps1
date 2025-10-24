# PowerShell script to install matplotlib and run CSV chart program
# Date: October 18, 2025

Write-Host "=== CSV Data Visualization Program ===" -ForegroundColor Green
Write-Host "This script will install matplotlib and run a Python program to generate a bar chart from CSV data" -ForegroundColor Yellow

# Check if Python is available
Write-Host "`nChecking Python installation..." -ForegroundColor Cyan
try {
    $pythonVersion = py --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Python not found. Please install Python first." -ForegroundColor Red
    exit 1
}

# Check if pip is available
Write-Host "`nChecking pip installation..." -ForegroundColor Cyan
try {
    $pipVersion = py -m pip --version 2>&1
    Write-Host "Pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: pip not found. Please install pip first." -ForegroundColor Red
    exit 1
}

# Install matplotlib
Write-Host "`nInstalling matplotlib..." -ForegroundColor Cyan
try {
    py -m pip install matplotlib
    Write-Host "Matplotlib installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "Warning: Error installing matplotlib. It may already be installed." -ForegroundColor Yellow
}

# Check matplotlib installation
Write-Host "`nVerifying matplotlib installation..." -ForegroundColor Cyan
$matplotlibCheck = py -c "import matplotlib; print('Matplotlib version:', matplotlib.__version__)" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host $matplotlibCheck -ForegroundColor Green
} else {
    Write-Host "Error: Matplotlib verification failed." -ForegroundColor Red
    Write-Host $matplotlibCheck -ForegroundColor Red
    exit 1
}

# List currently installed packages with matplotlib
Write-Host "`nListing installed packages (matplotlib-related)..." -ForegroundColor Cyan
try {
    py -m pip list | Select-String -Pattern "matplotlib|numpy|pyplot" -Context 0,0
} catch {
    Write-Host "Could not list packages." -ForegroundColor Yellow
}

# Run matplotlib test first
Write-Host "`nRunning matplotlib functionality test..." -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Yellow

try {
    py "test_matplotlib.py"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Test failed. Please check the errors above." -ForegroundColor Red
        Write-Host "Press any key to continue anyway..." -ForegroundColor Gray
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    } else {
        Write-Host "Tests passed successfully!" -ForegroundColor Green
    }
} catch {
    Write-Host "Error running test. Continuing with main program..." -ForegroundColor Yellow
}

# Run the chart generation program
Write-Host "`nRunning the CSV chart generation program..." -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Yellow

try {
    py "csv_chart_generator.py"
    Write-Host "`n=" * 50 -ForegroundColor Yellow
    Write-Host "Program completed successfully!" -ForegroundColor Green
    Write-Host "Check for the generated chart image file: sales_revenue_chart.png" -ForegroundColor Yellow
} catch {
    Write-Host "Error running the Python program." -ForegroundColor Red
    Write-Host $Error[0] -ForegroundColor Red
}

Write-Host "`nPress any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")