# Vercel Deployment Guide

This guide will walk you through deploying the PDF Merger application to Vercel.

## Prerequisites

- GitHub account
- Vercel account (you can sign up with your GitHub account)

## Deployment Steps

### Option 1: Deploy via GitHub

1. Push your code to a GitHub repository
2. Log in to Vercel (https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Configure the project:
   - Framework Preset: Other
   - Root Directory: ./
   - Build Command: Leave empty
   - Output Directory: Leave empty
6. Click "Deploy"

### Option 2: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Log in to Vercel:
   ```bash
   vercel login
   ```

3. Deploy the application:
   ```bash
   cd "path/to/pdf-merger"
   vercel --prod
   ```

## Important Notes

1. **Serverless Limitations**:
   - The PDF Merger on Vercel runs as a serverless function
   - File storage is temporary - files are not persisted between requests
   - Maximum PDF size may be limited due to serverless function constraints

2. **Configuration**:
   - The main entry point is `api/index.py`
   - Static files are served from the `static` directory
   - Templates are in the `templates` directory

3. **Troubleshooting**:
   - If deployment fails, check the Vercel deployment logs
   - Ensure all dependencies are correctly listed in `requirements.txt`
   - Make sure the Flask app is properly exported as `app` in `api/index.py`

## Monitoring

After deployment, you can:
- Monitor your application in the Vercel dashboard
- Set up custom domains
- View logs and deployment history
