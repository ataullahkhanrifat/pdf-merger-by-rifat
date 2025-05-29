#!/bin/bash

echo "Deploying PDF Merger to Vercel..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Login to Vercel if needed
vercel whoami &> /dev/null || vercel login

# Deploy to Vercel
echo "Deploying to Vercel..."
vercel --prod

echo "Deployment complete!"
echo "Visit your project dashboard to view the deployment status and logs."
