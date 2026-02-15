#!/bin/bash

# CIM Pattern - Automated Setup Script
# This script sets up the complete development environment

set -e

echo "=========================================="
echo "CIM Pattern - Automated Setup"
echo "=========================================="
echo ""

# Check Python version
echo "🐍 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Python $PYTHON_VERSION found"
echo ""

# Check Node.js version
echo "📦 Checking Node.js version..."
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found. Dashboard frontend won't be available."
    echo "   Install from: https://nodejs.org/"
    SKIP_FRONTEND=true
else
    NODE_VERSION=$(node --version)
    echo "✓ Node.js $NODE_VERSION found"
fi
echo ""

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt --quiet
echo "✓ Python dependencies installed"
echo ""

# Install Frontend dependencies (if Node.js available)
if [ "$SKIP_FRONTEND" != true ]; then
    echo "📥 Installing Frontend dependencies..."
    cd tools/dashboard/frontend
    npm install --silent
    cd ../../..
    echo "✓ Frontend dependencies installed"
    echo ""
fi

# Create .env from template
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your API keys!"
    echo ""
else
    echo "✓ .env file already exists"
    echo ""
fi

# Create config.local.yaml
if [ ! -f tools/curator-ai/config.local.yaml ]; then
    echo "📝 Creating config.local.yaml from template..."
    cp tools/curator-ai/config.yaml tools/curator-ai/config.local.yaml
    echo "✓ config.local.yaml created"
    echo ""
fi

# Run tests
echo "🧪 Running tests..."
pytest tests/unit/ -v --tb=short
if [ $? -eq 0 ]; then
    echo "✓ All tests passed!"
else
    echo "⚠️  Some tests failed. Check output above."
fi
echo ""

echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Edit .env and add your API keys"
echo "   nano .env"
echo ""
echo "2. Start the backend:"
echo "   python tools/dashboard/backend/api.py"
echo ""
if [ "$SKIP_FRONTEND" != true ]; then
    echo "3. Start the frontend (in another terminal):"
    echo "   cd tools/dashboard/frontend && npm start"
    echo ""
fi
echo "4. Try the Curator AI:"
echo "   python tools/curator-ai/monitor.py"
echo ""
echo "5. Read the Quick Start:"
echo "   docs/user/QUICKSTART.md"
echo ""
echo "=========================================="
echo ""
echo "For help: https://github.com/pyragogy/protocols"
echo ""
