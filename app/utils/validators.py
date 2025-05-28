from flask import current_app
from app.utils.file_utils import FileUtils

def validate_file(file):
    """
    Validate uploaded file
    
    Args:
        file: File object from request
        
    Returns:
        dict: Validation result with 'valid' boolean and 'error' message
    """
    # Check if file exists
    if not file or file.filename == '':
        return {'valid': False, 'error': 'No file selected'}
    
    # Check file extension
    if not FileUtils.allowed_file(file.filename):
        return {'valid': False, 'error': 'Only PDF files are allowed'}
    
    # Check file size (Flask handles this automatically with MAX_CONTENT_LENGTH)
    # But we can add additional validation here if needed
    
    return {'valid': True, 'error': None}

def validate_merge_request(data):
    """
    Validate merge request data
    
    Args:
        data (dict): Request data
        
    Returns:
        dict: Validation result
    """
    if not data:
        return {'valid': False, 'error': 'No data provided'}
    
    if 'files' not in data:
        return {'valid': False, 'error': 'No files specified'}
    
    if not isinstance(data['files'], list) or len(data['files']) < 2:
        return {'valid': False, 'error': 'At least 2 files are required for merging'}
    
    if 'session_id' not in data:
        return {'valid': False, 'error': 'Session ID is required'}
    
    return {'valid': True, 'error': None}
