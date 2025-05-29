# 🔄 PDF Merger Application
*Developed by **Md Ataullah Khan Rifat***

A professional, secure, and user-friendly web-based PDF merging tool built with Flask and modern web technologies.

## 🚀 **QUICK START - Choose Your Method**

### 🐳 **Method 1: Docker (EASIEST)**
*No Python installation required! Works on any system.*

```bash
git clone https://github.com/ataullahkhanrifat/pdf-merger-by-rifat
cd pdf-merger-by-rifat
docker-compose up --build
```
**🎉 Done!** Open http://localhost:5000

---

### ⚡ **Method 2: One-Click Setup**

**Windows Users:**
```bash
git clone https://github.com/ataullahkhanrifat/pdf-merger-by-rifat
cd pdf-merger-by-rifat
setup.bat
```

**Linux/Mac Users:**
```bash
git clone https://github.com/ataullahkhanrifat/pdf-merger-by-rifat
cd pdf-merger-by-rifat
chmod +x setup.sh && ./setup.sh
```

---

### 🛠️ **Method 3: Manual Setup**
*For developers who want full control*

```bash
git clone https://github.com/ataullahkhanrifat/pdf-merger-by-rifat
cd pdf-merger-by-rifat

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

## 📋 System Requirements

| Method | Requirements |
|--------|-------------|
| **Docker** | Docker & Docker Compose only |
| **Automated** | Python 3.7+ |
| **Manual** | Python 3.7+, pip, venv |

## ✨ Features

- 🖱️ **Drag & Drop**: Intuitive file upload
- 🔄 **Reorder Files**: Change merge order easily
- 📱 **Mobile Responsive**: Works on all devices
- 🔒 **Secure**: File validation and cleanup
- ⚡ **Fast Processing**: Optimized PDF engine
- 🎨 **Modern UI**: Beautiful Tailwind CSS design

## 🏗️ Architecture

```
pdf-merger-by-rifat/
├── app/
│   ├── routes.py          # API endpoints
│   ├── services/          # PDF processing logic
│   ├── utils/             # Utilities & validation
│   └── templates/         # Frontend UI
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Easy deployment
├── requirements.txt       # Python dependencies
└── setup.sh/.bat         # Automated setup
```

## 🚀 Deployment Options

- **Local Development**: `docker-compose up`
- **Heroku**: `git push heroku main`
- **AWS/GCP**: Deploy container directly
- **VPS**: Docker Compose on any server

## 👨‍💻 Developer

**Md Ataullah Khan Rifat**
- GitHub: [@ataullahkhanrifat](https://github.com/ataullahkhanrifat)
- Email: ataullahkhan.rifat@gmail.com

---

⭐ **Star this repository if you find it useful!**
