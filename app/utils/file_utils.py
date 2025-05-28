from werkzeug.utils import secure_filename
from flask import current_app
import os
import uuid

class FileUtils:
    @staticmethod
    def secure_filename(filename):
        """
        Generate a secure filename
        
        Args:
            filename (str): Original filename
            
        Returns:
            str: Secure filename
        """
        # Use werkzeug's secure_filename and add timestamp for uniqueness
        base_filename = secure_filename(filename)
        name, ext = os.path.splitext(base_filename)
        return f"{name}_{uuid.uuid4().hex[:8]}{ext}"
    
    @staticmethod
    def save_file(file, filename, session_id):
        """
        Save uploaded file
        
        Args:
            file: File object from request
            filename (str): Secure filename
            session_id (str): Session identifier
            
        Returns:
            str: Path to saved file
        """
        # Create session directory
        session_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], session_id)
        os.makedirs(session_dir, exist_ok=True)
        
        file_path = os.path.join(session_dir, filename)
        file.save(file_path)
        
        return file_path
    
    @staticmethod
    def get_file_size(file_path):
        """
        Get file size in bytes
        
        Args:
            file_path (str): Path to file
            
        Returns:
            int: File size in bytes
        """
        try:
            return os.path.getsize(file_path)
        except OSError:
            return 0
    
    @staticmethod
    def format_file_size(size_bytes):
        """
        Format file size in human readable format
        
        Args:
            size_bytes (int): Size in bytes
            
        Returns:
            str: Formatted size string
        """
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"
    
    @staticmethod
    def cleanup_session_files(session_id):
        """
        Clean up files for a session
        
        Args:
            session_id (str): Session identifier
        """
        try:
            session_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], session_id)
            if os.path.exists(session_dir):
                import shutil
                shutil.rmtree(session_dir)
        except Exception as e:
            current_app.logger.error(f"Error cleaning up session {session_id}: {str(e)}")
    
    @staticmethod
    def allowed_file(filename):
        """
        Check if file extension is allowed
        
        Args:
            filename (str): Filename to check
            
        Returns:
            bool: True if allowed, False otherwise
        """
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
