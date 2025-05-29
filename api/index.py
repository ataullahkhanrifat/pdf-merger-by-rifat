from flask import Flask, render_template, request, jsonify, send_file
import os
import uuid
from PyPDF2 import PdfMerger
from werkzeug.utils import secure_filename
import logging
import traceback
import tempfile

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Use temp directory for uploads in serverless
UPLOAD_FOLDER = tempfile.gettempdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
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
            if file and file.filename.lower().endswith('.pdf'):
                filename = secure_filename(file.filename)
                unique_filename = f"{session_id}_{filename}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                file.save(file_path)
                
                # Verify the file was saved correctly
                if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                    uploaded_files.append({
                        'id': str(uuid.uuid4()),
                        'name': filename,
                        'path': unique_filename,
                        'size': os.path.getsize(file_path)
                    })
                    logger.info(f"Successfully uploaded: {filename} ({os.path.getsize(file_path)} bytes)")
                else:
                    logger.error(f"Failed to save file: {filename}")
        
        if not uploaded_files:
            return jsonify({'error': 'No valid PDF files were uploaded'}), 400
        
        return jsonify({
            'success': True,
            'files': uploaded_files,
            'session_id': session_id
        })
    
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': f'Upload failed: {str(e)}'}), 500

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    """Merge PDF files with improved error handling for unlimited files"""
    try:
        data = request.get_json()
        if not data or 'files' not in data:
            return jsonify({'error': 'Invalid request data'}), 400
        
        files = data['files']
        if len(files) < 2:
            return jsonify({'error': 'At least 2 PDF files are required for merging'}), 400
        
        logger.info(f"Starting merge process for {len(files)} files")
        
        # Create a new PdfMerger instance
        merger = PdfMerger()
        valid_files = 0
        failed_files = []
        
        try:
            # Add each file to the merger
            for i, file_info in enumerate(files):
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_info['path'])
                
                if not os.path.exists(file_path):
                    logger.error(f"File not found: {file_path}")
                    failed_files.append(file_info['name'])
                    continue
                
                if os.path.getsize(file_path) == 0:
                    logger.error(f"File is empty: {file_path}")
                    failed_files.append(file_info['name'])
                    continue
                
                try:
                    # Add the file to merger
                    logger.info(f"Adding file {i+1}/{len(files)}: {file_info['name']}")
                    
                    # Open and append the PDF file
                    with open(file_path, 'rb') as pdf_file:
                        merger.append(pdf_file)
                    
                    valid_files += 1
                    logger.info(f"Successfully added: {file_info['name']}")
                    
                except Exception as file_error:
                    logger.error(f"Error adding file {file_info['name']}: {str(file_error)}")
                    failed_files.append(file_info['name'])
                    continue
            
            if valid_files < 2:
                merger.close()
                error_msg = f'Only {valid_files} valid files found. At least 2 are required.'
                if failed_files:
                    error_msg += f' Failed files: {", ".join(failed_files)}'
                return jsonify({'error': error_msg}), 400
            
            # Generate output filename
            output_filename = f"merged_{uuid.uuid4().hex}.pdf"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            
            # Write the merged PDF
            logger.info(f"Writing merged PDF to: {output_path}")
            with open(output_path, 'wb') as output_file:
                merger.write(output_file)
            
            # Close the merger
            merger.close()
            
            # Verify the output file was created
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                logger.info(f"Merge successful! Output file size: {os.path.getsize(output_path)} bytes")
                
                success_msg = {
                    'success': True,
                    'download_url': f'/download/{output_filename}',
                    'filename': output_filename,
                    'merged_files': valid_files
                }
                
                if failed_files:
                    success_msg['warning'] = f'Successfully merged {valid_files} files. Failed files: {", ".join(failed_files)}'
                
                return jsonify(success_msg)
            else:
                logger.error("Output file was not created or is empty")
                return jsonify({'error': 'Failed to create merged PDF'}), 500
                
        except Exception as merge_error:
            # Make sure to close the merger in case of error
            try:
                merger.close()
            except:
                pass
            raise merge_error
    
    except Exception as e:
        logger.error(f"Merge error: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': f'Merge failed: {str(e)}'}), 500

@app.route('/download/<filename>')
def download_file(filename):
    """Download merged PDF"""
    try:
        # Security check - only allow downloads from uploads folder
        if not filename.endswith('.pdf') or '..' in filename:
            return jsonify({'error': 'Invalid filename'}), 400
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        if os.path.exists(file_path):
            logger.info(f"Downloading file: {filename}")
            return send_file(
                file_path, 
                as_attachment=True, 
                download_name=f"merged_pdfs_{filename}",
                mimetype='application/pdf'
            )
        else:
            logger.error(f"Download file not found: {file_path}")
            return jsonify({'error': 'File not found'}), 404
            
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        return jsonify({'error': 'Download failed'}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'pdf-merger',
        'version': '1.0.0'
    })

# Export the app for Vercel
app = app