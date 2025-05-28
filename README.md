# PDF Merger Application

A modern, web-based PDF merger application built with Flask and featuring a clean, responsive UI with drag-and-drop functionality.

**Developed by Md Ataullah Khan Rifat** - Full Stack Developer & Software Engineer

## Features

- **Drag & Drop Interface**: Intuitive file upload with drag-and-drop support
- **File Reordering**: Drag files to reorder them before merging
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Real-time Feedback**: Progress indicators and error handling
- **Secure Processing**: Files are processed locally and automatically cleaned up
- **Docker Support**: Fully containerized for easy deployment
- **Clean Architecture**: Well-structured codebase with separation of concerns

## Architecture

```
app/
├── __init__.py
├── config.py              # Application configuration
├── routes.py              # API routes and endpoints
├── services/
│   ├── __init__.py
│   └── pdf_service.py     # PDF processing logic
├── utils/
│   ├── __init__.py
│   ├── file_utils.py      # File handling utilities
│   └── validators.py      # Input validation
└── templates/
    └── index.html         # Frontend template
```

## Quick Start

### Local Development

#### Option 1: Automated Setup
- **Windows**: Run `setup.bat`
- **Linux/Mac**: Run `chmod +x setup.sh && ./setup.sh`

#### Option 2: Manual Setup
1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   # or for more options:
   python run.py --env development --debug
   ```

5. **Open browser**: Navigate to `http://localhost:5000`

#### Testing Setup
```bash
python test_setup.py
```

### Docker Deployment

1. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

2. **For production with nginx**:
   ```bash
   docker-compose --profile production up --build
   ```

## API Endpoints

- `GET /` - Main application page
- `POST /upload` - Upload PDF files
- `POST /merge` - Merge uploaded PDFs
- `GET /download/<filename>` - Download merged PDF

## Configuration

Key configuration options in `app/config.py`:

- `MAX_CONTENT_LENGTH`: Maximum file size (default: 50MB)
- `UPLOAD_FOLDER`: Directory for temporary file storage
- `SECRET_KEY`: Flask session secret (change in production)

## Security Features

- File type validation (PDF only)
- File size limits
- Secure filename generation
- Automatic cleanup of temporary files
- Input sanitization and validation

## Dependencies

- **Flask**: Web framework
- **pypdf**: PDF processing library
- **Werkzeug**: WSGI utilities
- **Gunicorn**: Production WSGI server
- **Tailwind CSS**: Frontend styling
- **SortableJS**: Drag-and-drop functionality

## Development

### Project Structure

The application follows a clean architecture pattern:

- **Routes** (`routes.py`): Handle HTTP requests and responses
- **Services** (`services/`): Business logic and PDF processing
- **Utils** (`utils/`): Utility functions and validators
- **Templates** (`templates/`): HTML templates and frontend code

### Adding New Features

1. **Backend**: Add new routes in `routes.py` and business logic in appropriate service modules
2. **Frontend**: Extend the JavaScript functionality in `index.html`
3. **Validation**: Add new validators in `utils/validators.py`

## Deployment

### Environment Variables

- `SECRET_KEY`: Flask secret key for sessions
- `FLASK_ENV`: Environment (development/production)
- `MAX_CONTENT_LENGTH`: Maximum upload size

### Production Considerations

- Use environment-specific secret keys
- Configure proper logging
- Set up monitoring and health checks
- Use SSL/TLS certificates
- Configure rate limiting if needed

## License

This project is created by **Md Ataullah Khan Rifat** as a professional PDF merger solution showcasing modern web development practices.

## Developer

**Md Ataullah Khan Rifat**
- Full Stack Developer & Software Engineer
- Expertise in Python, Flask, and modern web technologies
- Focus on clean architecture and user experience design

## Contributing

1. Follow the existing code structure
2. Add proper error handling
3. Include input validation
4. Write clear comments
5. Test thoroughly before submitting
