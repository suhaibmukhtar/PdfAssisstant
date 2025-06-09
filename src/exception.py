from logger import logging
import sys


def get_error_message_details(error_message: str, error_message_detail: sys) -> str:
    """
    Extracts and formats the error message details from the exception.
    
    Args:
        error_message (str): The error message string.
        error_message_detail (sys): The sys module to extract exception details.
        
    Returns:
        str: A formatted string containing the error message and details.
    """
    _, _, exc_tb = error_message_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {error_message}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_message_detail: sys):
        super().__init__(error_message)
        self.message = get_error_message_details(error_message, error_message_detail)
        
    def __str__(self):
        logging.error(self.message)
        return self.message