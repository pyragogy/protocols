#!/bin/bash

# CIM Pattern v3.0 - Quick Deploy Script
# This script helps you commit the new structure to your repository

set -e  # Exit on error

echo "=========================================="
echo "CIM Pattern v3.0 - Deploy Script"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Run this script from the protocols-v3 directory"
    exit 1
fi

echo "✓ Found README.md"
echo ""

# Check git status
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "📦 Initializing git repository..."
    git init
    echo "✓ Git initialized"
else
    echo "✓ Git repository detected"
fi

echo ""
echo "📊 Current structure:"
echo "---"
tree -L 2 -I '__pycache__|*.pyc' || ls -R
echo "---"
echo ""

# Ask for confirmation
echo "This will:"
echo "  1. Add all files to git"
echo "  2. Create a commit with message: 'v3.0: Production-ready foundation'"
echo "  3. Ready for push to GitHub"
echo ""
read -p "Continue? (y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelled"
    exit 1
fi

# Add all files
echo ""
echo "📝 Staging files..."
git add .

# Show what will be committed
echo ""
echo "📋 Files to be committed:"
git status --short

# Create commit
echo ""
echo "💾 Creating commit..."
git commit -m "v3.0: Production-ready foundation

Major rewrite from manifesto to production-ready system.

Added:
- Zc Calculator (web + CLI)
- Slack webhook integration
- GUSH & BHO templates
- Complete documentation rewrite
- Quick start guide
- Real-world examples

Changed:
- Repository structure (tools/, docs/, examples/)
- Focus from theory to practice
- README from academic to operational

See CHANGELOG.md for full details."

echo ""
echo "✅ Commit created successfully!"
echo ""

# Instructions for pushing
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo ""
echo "If this is a new repository:"
echo "  1. Create repo on GitHub: https://github.com/new"
echo "  2. Run these commands:"
echo ""
echo "     git remote add origin git@github.com:YOUR_USERNAME/protocols.git"
echo "     git branch -M main"
echo "     git push -u origin main"
echo ""
echo "If updating existing repository:"
echo "  1. Merge with existing:"
echo ""
echo "     git remote add old https://github.com/pyragogy/protocols.git"
echo "     git fetch old"
echo "     git merge old/main --allow-unrelated-histories"
echo ""
echo "  2. Then push:"
echo ""
echo "     git push origin main"
echo ""
echo "=========================================="
echo ""
echo "🚀 Ready to ship v3.0!"
echo ""
