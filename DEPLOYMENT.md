# PDF Merger - Deployment Guide

## Prerequisites

### Local Development
- Python 3.8 or higher
- pip (Python package installer)

### Docker Deployment
- Docker Desktop (for Windows/Mac) or Docker Engine (for Linux)
- Docker Compose

## Setup Options

### Option 1: Local Development Setup

#### Windows
1. Run the setup script:
   ```cmd
   setup.bat
   ```

#### Linux/Mac
1. Make the setup script executable and run it:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

#### Manual Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open browser and navigate to: `http://localhost:5000`

### Option 2: Docker Deployment

#### Development Mode
```bash
docker-compose up --build
```

#### Production Mode (with nginx)
```bash
docker-compose --profile production up --build
```

## Configuration

### Environment Variables
Create a `.env` file for production:

```env
SECRET_KEY=your-very-secure-secret-key-here
FLASK_ENV=production
MAX_CONTENT_LENGTH=52428800  # 50MB in bytes
```

### Security Considerations
- Change the default SECRET_KEY in production
- Use HTTPS in production environments
- Configure firewall rules appropriately
- Set up monitoring and logging

## Usage

1. **Upload PDFs**: Drag and drop or click to select PDF files
2. **Reorder**: Drag files to change merge order
3. **Remove**: Click trash icon to remove individual files
4. **Merge**: Click "Merge PDFs" button
5. **Download**: Click "Download PDF" to get the merged file

## Troubleshooting

### Common Issues

1. **Port already in use**:
   - Change port in app.py or docker-compose.yml
   - Stop other services using port 5000

2. **File upload fails**:
   - Check file size (max 50MB)
   - Ensure files are valid PDFs
   - Check disk space

3. **Docker issues**:
   - Ensure Docker is running
   - Check Docker permissions
   - Try rebuilding: `docker-compose build --no-cache`

### Logs
- Local: Check terminal output
- Docker: `docker-compose logs pdf-merger`

## API Documentation

### Upload Files
```http
POST /upload
Content-Type: multipart/form-data

Form data:
- files: PDF files (multiple)
```

### Merge PDFs
```http
POST /merge
Content-Type: application/json

{
  "files": [
    {"id": "...", "name": "...", "path": "..."},
    ...
  ],
  "session_id": "..."
}
```

### Download Merged PDF
```http
GET /download/<filename>
```

## Development

### Project Structure
```
app/
├── config.py          # Configuration settings
├── routes.py          # API endpoints
├── services/          # Business logic
│   └── pdf_service.py # PDF processing
├── utils/             # Utilities
│   ├── file_utils.py  # File operations
│   └── validators.py  # Input validation
└── templates/         # Frontend
    └── index.html     # Main UI
```

### Adding Features
1. Backend: Add routes in `routes.py`, logic in `services/`
2. Frontend: Extend JavaScript in `index.html`
3. Validation: Add validators in `utils/validators.py`

## Performance Tuning

### Production Settings
- Use Gunicorn with multiple workers
- Configure nginx for static files
- Set up Redis for session storage (if needed)
- Use proper logging configuration

### Scaling
- Use load balancer for multiple instances
- Configure shared storage for uploads
- Add monitoring (Prometheus, Grafana)
- Set up health checks
