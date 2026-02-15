#!/bin/bash

# Quick Deploy Script
# Starts backend and frontend in development mode

set -e

echo "🚀 Starting CIM Pattern - Curator AI"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "Run: cp .env.example .env"
    echo "Then edit .env with your API keys"
    exit 1
fi

# Source .env
export $(cat .env | grep -v '^#' | xargs)

# Check ANTHROPIC_API_KEY
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  Warning: ANTHROPIC_API_KEY not set"
    echo "AI recommendations will not work"
    echo ""
fi

echo "Starting Backend API..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start backend in background
python tools/dashboard/backend/api.py &
BACKEND_PID=$!

echo "Backend started (PID: $BACKEND_PID)"
echo "API running at: http://localhost:8000"
echo "API docs at: http://localhost:8000/docs"
echo ""

# Wait for backend to start
sleep 3

# Check if frontend dependencies are installed
if [ ! -d "tools/dashboard/frontend/node_modules" ]; then
    echo "Installing frontend dependencies..."
    cd tools/dashboard/frontend
    npm install
    cd ../../..
fi

echo "Starting Frontend..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start frontend
cd tools/dashboard/frontend
npm start &
FRONTEND_PID=$!
cd ../../..

echo "Frontend started (PID: $FRONTEND_PID)"
echo "Dashboard will open at: http://localhost:3000"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Both services running!"
echo ""
echo "Press Ctrl+C to stop both services"
echo ""

# Trap Ctrl+C and kill both processes
trap "echo ''; echo 'Stopping services...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT

# Wait for user to stop
wait
