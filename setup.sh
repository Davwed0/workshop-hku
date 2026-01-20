#!/bin/bash
# Setup script for Python Workshop
# This script helps you set up the workshop environment quickly

echo "=========================================="
echo "Python Workshop Setup Script"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python is installed"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Mac/Linux
    source venv/bin/activate
fi

if [ $? -ne 0 ]; then
    echo "⚠️  Could not activate virtual environment automatically."
    echo "Please run:"
    echo "  On Windows: venv\\Scripts\\activate"
    echo "  On Mac/Linux: source venv/bin/activate"
    exit 1
fi

echo "✓ Virtual environment activated"
echo ""

# Install requirements
echo "Installing required packages..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

if [ $? -ne 0 ]; then
    echo "❌ Package installation failed."
    echo "Try running: pip install -r requirements.txt"
    exit 1
fi

echo "✓ Packages installed successfully"
echo ""

# Run tests
echo "Running validation tests..."
python3 test_notebooks.py

if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  Some tests failed. Please check the errors above."
    exit 1
fi

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "To start the workshop:"
echo "  1. Make sure virtual environment is activated"
echo "  2. Run: jupyter notebook"
echo "  3. Open notebooks/01_basics.ipynb"
echo ""
echo "Have fun learning! 🚀"
