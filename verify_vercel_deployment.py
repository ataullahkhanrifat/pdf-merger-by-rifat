#!/usr/bin/env python
"""
This script validates the project structure for Vercel deployment.
Run this before deploying to check for common issues.
"""

import os
import sys

def check_project_structure():
    """Check if the project structure is correct for Vercel deployment"""
    errors = []
    warnings = []
    
    # Check if api/index.py exists
    if not os.path.exists("api/index.py"):
        errors.append("Missing api/index.py file")
    else:
        print("✓ Found api/index.py")
    
    # Check if vercel.json exists
    if not os.path.exists("vercel.json"):
        errors.append("Missing vercel.json file")
    else:
        print("✓ Found vercel.json")
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        errors.append("Missing requirements.txt file")
    else:
        print("✓ Found requirements.txt")
        
        # Check requirements content
        with open("requirements.txt", "r") as f:
            content = f.read()
            if "Flask" not in content:
                errors.append("Flask not found in requirements.txt")
            else:
                print("✓ Flask found in requirements.txt")
            
            if "PyPDF2" not in content:
                errors.append("PyPDF2 not found in requirements.txt")
            else:
                print("✓ PyPDF2 found in requirements.txt")
    
    # Check if templates directory exists
    if not os.path.exists("templates"):
        warnings.append("templates directory not found at root level")
    else:
        print("✓ Found templates directory")
    
    # Check if static directory exists
    if not os.path.exists("static"):
        warnings.append("static directory not found at root level")
    else:
        print("✓ Found static directory")
    
    # Report results
    if errors:
        print("\n❌ Found errors that will prevent deployment:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\n✓ No critical errors found")
    
    if warnings:
        print("\n⚠️ Warnings (may not prevent deployment but could cause issues):")
        for warning in warnings:
            print(f"  - {warning}")
    
    return len(errors) == 0

if __name__ == "__main__":
    print("Checking project structure for Vercel deployment...")
    success = check_project_structure()
    
    if success:
        print("\n✅ Project structure looks good for Vercel deployment!")
        print("You can now deploy with 'vercel' or connect your GitHub repository to Vercel.")
    else:
        print("\n❌ Please fix the errors above before deploying to Vercel.")
        sys.exit(1)
