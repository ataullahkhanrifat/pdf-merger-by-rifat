# PDF Merger Application

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

A modern PDF merging tool that combines multiple PDF files into one. Built with Flask and Docker.

**Developed by: Md Ataullah Khan Rifat**

## ✨ Features

- 🔄 **Unlimited PDF Merging** - Combine as many PDF files as you want
- 🎯 **Drag & Drop Interface** - Easy file upload
- 📋 **File Reordering** - Drag to reorder files before merging
- 🔒 **Secure & Private** - Files automatically deleted after processing
- 🐳 **Docker Ready** - Easy deployment

## 🚀 Quick Start (Docker - Recommended)

### Prerequisites
- Docker
- Docker Compose

### Installation

1. **Navigate to project**
   ```bash
   cd "C:\Users\Rifat PC\Documents\Pdf Merger"
   ```

2. **Add your photo**
   ```bash
   cp Photo/* static/images/CV_Photo.jpg
   ```

3. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

4. **Access**: `http://localhost:5000`

## 🐍 Without Docker (Manual Setup)

### Prerequisites
- Python 3.8+ installed

### Installation

1. **Navigate to project**
   ```bash
   cd "C:\Users\Rifat PC\Documents\Pdf Merger"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Add your photo**
   ```bash
   mkdir static\images
   copy Photo\* static\images\CV_Photo.jpg
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access**: `http://localhost:5000`

## 📋 Usage

1. Upload PDF files (drag & drop or click)
2. Reorder files if needed
3. Click "Merge PDFs"
4. Download merged file

## ⚙️ Limits

- **Max file size**: 50MB per PDF
- **Number of files**: Unlimited
- **Format**: PDF only

## 🐛 Troubleshooting

**Port 5000 in use?** Change port in `docker-compose.yml`:
```yaml
ports:
  - "5001:5000"
```

**Photo not showing?** Copy again:
```bash
cp Photo/* static/images/CV_Photo.jpg
```

**Python not found?** Install from: https://www.python.org/downloads/

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ by Md Ataullah Khan Rifat**
