#!/bin/bash

# Classical Philosophy Text Analysis - Run Script
# This script runs the analysis and starts a web server

echo "================================================"
echo "Classical Philosophy Text Analysis"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if required packages are installed
echo "📦 Checking dependencies..."
python3 -c "import docx, wordcloud, matplotlib, nltk, textblob" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Some dependencies are missing. Installing..."
    pip install python-docx wordcloud matplotlib nltk textblob pillow
fi

echo "✅ Dependencies OK"
echo ""

# Run the analysis
echo "🔍 Running text analysis..."
echo "This may take a few minutes..."
echo ""
python3 analyze_texts.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Analysis complete!"
    echo ""
    echo "================================================"
    echo "Starting web server..."
    echo "================================================"
    echo ""
    echo "📊 Open your browser to: http://localhost:8000"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo ""

    cd output
    python3 -m http.server 8000
else
    echo "❌ Analysis failed. Please check the error messages above."
    exit 1
fi
