#!/bin/bash
# This script deploys the application to Vercel

echo "Deploying to Vercel..."
echo "Checking for Vercel CLI..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null
then
    echo "Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Deploy to Vercel
echo "Deploying to Vercel..."
vercel --prod

echo "Deployment complete!"
