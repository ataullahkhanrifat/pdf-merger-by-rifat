from pypdf import PdfWriter, PdfReader
from flask import current_app
import os

class PDFService:
    @staticmethod
    def merge_pdfs(file_paths, output_filename):
        """
        Merge multiple PDF files into one
        
        Args:
            file_paths (list): List of PDF file paths to merge
            output_filename (str): Name of the output file
            
        Returns:
            str: Path to the merged PDF file or None if failed
        """
        try:
            pdf_writer = PdfWriter()
            
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    current_app.logger.error(f"File not found: {file_path}")
                    continue
                
                try:
                    pdf_reader = PdfReader(file_path)
                    
                    # Add all pages from the current PDF
                    for page in pdf_reader.pages:
                        pdf_writer.add_page(page)
                        
                except Exception as e:
                    current_app.logger.error(f"Error reading PDF {file_path}: {str(e)}")
                    continue
            
            # Write the merged PDF
            output_path = os.path.join(current_app.config['UPLOAD_FOLDER'], output_filename)
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            current_app.logger.info(f"Successfully merged {len(file_paths)} PDFs into {output_filename}")
            return output_path
            
        except Exception as e:
            current_app.logger.error(f"Error merging PDFs: {str(e)}")
            return None
    
    @staticmethod
    def validate_pdf(file_path):
        """
        Validate if a file is a valid PDF
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            bool: True if valid PDF, False otherwise
        """
        try:
            with open(file_path, 'rb') as file:
                PdfReader(file)
            return True
        except Exception as e:
            current_app.logger.error(f"Invalid PDF {file_path}: {str(e)}")
            return False
    
    @staticmethod
    def get_pdf_page_count(file_path):
        """
        Get the number of pages in a PDF
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            int: Number of pages or 0 if error
        """
        try:
            pdf_reader = PdfReader(file_path)
            return len(pdf_reader.pages)
        except Exception as e:
            current_app.logger.error(f"Error counting pages in {file_path}: {str(e)}")
            return 0
