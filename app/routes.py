from flask import Blueprint, render_template, request, jsonify, send_file, send_from_directory, current_app
from app.services.pdf_service import PDFService
from app.utils.file_utils import FileUtils
from app.utils.validators import validate_file
import os
import uuid

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@main_bp.route('/upload', methods=['POST'])
def upload_files():
    """Handle file upload"""
    try:
        if 'files' not in request.files:
            return jsonify({'error': 'No files provided'}), 400
        
        files = request.files.getlist('files')
        if not files or files[0].filename == '':
            return jsonify({'error': 'No files selected'}), 400
        
        uploaded_files = []
        session_id = str(uuid.uuid4())
        
        for file in files:
            # Validate file
            validation_result = validate_file(file)
            if not validation_result['valid']:
                return jsonify({'error': validation_result['error']}), 400
            
            # Save file
            filename = FileUtils.secure_filename(file.filename)
            file_path = FileUtils.save_file(file, filename, session_id)
            
            uploaded_files.append({
                'id': str(uuid.uuid4()),
                'name': filename,
                'original_name': file.filename,
                'path': file_path,
                'size': FileUtils.get_file_size(file_path)
            })
        
        return jsonify({
            'success': True,
            'files': uploaded_files,
            'session_id': session_id
        })
    
    except Exception as e:
        current_app.logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': 'Upload failed'}), 500

@main_bp.route('/merge', methods=['POST'])
def merge_pdfs():
    """Merge PDF files"""
    try:
        data = request.get_json()
        if not data or 'files' not in data or 'session_id' not in data:
            return jsonify({'error': 'Invalid request data'}), 400
        
        file_paths = []
        for file_info in data['files']:
            if 'path' not in file_info:
                return jsonify({'error': 'Invalid file data'}), 400
            file_paths.append(file_info['path'])
        
        # Merge PDFs
        output_filename = f"merged_{data['session_id']}.pdf"
        output_path = PDFService.merge_pdfs(file_paths, output_filename)
        
        if not output_path:
            return jsonify({'error': 'Failed to merge PDFs'}), 500
        
        return jsonify({
            'success': True,
            'download_url': f'/download/{output_filename}',
            'filename': output_filename
        })
    
    except Exception as e:
        current_app.logger.error(f"Merge error: {str(e)}")
        return jsonify({'error': 'Merge failed'}), 500

@main_bp.route('/download/<filename>')
def download_file(filename):
    """Download merged PDF"""
    try:
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
    
    except Exception as e:
        current_app.logger.error(f"Download error: {str(e)}")
        return jsonify({'error': 'Download failed'}), 500

@main_bp.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 50MB.'}), 413

@main_bp.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'service': 'pdf-merger',
        'version': '1.0.0'
    }), 200

@main_bp.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'error': 'Resource not found'}), 404

@main_bp.errorhandler(500)
def internal_error(e):
    """Handle internal server errors"""
    current_app.logger.error(f"Internal error: {str(e)}")
    return jsonify({'error': 'Internal server error'}), 500
