#!/usr/bin/env python3
"""
PDF Merger Application Runner
Supports different environments and configurations.
"""

import os
import sys
import argparse
from app import create_app

def main():
    parser = argparse.ArgumentParser(description='PDF Merger Application')
    parser.add_argument(
        '--env', 
        choices=['development', 'production'], 
        default='development',
        help='Environment to run in (default: development)'
    )
    parser.add_argument(
        '--host', 
        default='0.0.0.0',
        help='Host to bind to (default: 0.0.0.0)'
    )
    parser.add_argument(
        '--port', 
        type=int, 
        default=5000,
        help='Port to bind to (default: 5000)'
    )
    parser.add_argument(
        '--debug', 
        action='store_true',
        help='Enable debug mode'
    )
    
    args = parser.parse_args()
    
    # Set environment variable
    os.environ['FLASK_ENV'] = args.env
    
    # Create application
    app = create_app()
    
    # Configure based on environment
    if args.env == 'production':
        # Production settings
        debug_mode = False
        print(f"Starting PDF Merger in PRODUCTION mode on {args.host}:{args.port}")
        print("Note: For production, consider using gunicorn:")
        print(f"  gunicorn --bind {args.host}:{args.port} --workers 4 'app:create_app()'")
    else:
        # Development settings
        debug_mode = args.debug or True
        print(f"Starting PDF Merger in DEVELOPMENT mode on {args.host}:{args.port}")
    
    # Ensure uploads directory exists
    uploads_dir = os.path.join(os.path.dirname(__file__), 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)
    
    print(f"Uploads directory: {uploads_dir}")
    print(f"Access the application at: http://localhost:{args.port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        app.run(
            host=args.host,
            port=args.port,
            debug=debug_mode,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\nShutting down PDF Merger application...")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
