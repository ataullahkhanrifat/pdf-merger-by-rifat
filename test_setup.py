#!/usr/bin/env python3
"""
Test script to validate the PDF Merger application structure and basic functionality.
Run this after installing dependencies to ensure everything is set up correctly.
"""

import os
import sys
import importlib.util

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description}: {filepath} (NOT FOUND)")
        return False

def check_import(module_name):
    """Check if a module can be imported"""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            print(f"✓ Module '{module_name}' is available")
            return True
        else:
            print(f"✗ Module '{module_name}' is NOT available")
            return False
    except ImportError:
        print(f"✗ Module '{module_name}' is NOT available")
        return False

def main():
    print("PDF Merger Application - Structure Validation")
    print("=" * 50)
    
    # Check project structure
    print("\n1. Checking project structure...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    files_to_check = [
        ("app.py", "Main application file"),
        ("requirements.txt", "Dependencies file"),
        ("Dockerfile", "Docker configuration"),
        ("docker-compose.yml", "Docker Compose configuration"),
        ("README.md", "Documentation"),
        ("app/__init__.py", "App package init"),
        ("app/config.py", "Configuration module"),
        ("app/routes.py", "Routes module"),
        ("app/services/__init__.py", "Services package init"),
        ("app/services/pdf_service.py", "PDF service module"),
        ("app/utils/__init__.py", "Utils package init"),
        ("app/utils/file_utils.py", "File utilities module"),
        ("app/utils/validators.py", "Validators module"),
        ("app/templates/index.html", "Main template"),
    ]
    
    structure_ok = True
    for filename, description in files_to_check:
        filepath = os.path.join(base_dir, filename)
        if not check_file_exists(filepath, description):
            structure_ok = False
    
    # Check dependencies
    print("\n2. Checking Python dependencies...")
    dependencies = [
        "flask",
        "pypdf", 
        "werkzeug",
        "gunicorn"
    ]
    
    deps_ok = True
    for dep in dependencies:
        if not check_import(dep):
            deps_ok = False
    
    # Summary
    print("\n" + "=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    
    if structure_ok:
        print("✓ Project structure: OK")
    else:
        print("✗ Project structure: ISSUES FOUND")
    
    if deps_ok:
        print("✓ Dependencies: OK")
        print("\nYou can now run the application:")
        print("  python app.py")
    else:
        print("✗ Dependencies: MISSING")
        print("\nTo install dependencies:")
        print("  pip install -r requirements.txt")
    
    # Additional checks
    uploads_dir = os.path.join(base_dir, "uploads")
    if not os.path.exists(uploads_dir):
        print(f"\nNote: Creating uploads directory: {uploads_dir}")
        os.makedirs(uploads_dir, exist_ok=True)
    
    return structure_ok and deps_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
