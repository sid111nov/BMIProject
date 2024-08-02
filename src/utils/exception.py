import sys
from src.utils.logger import logger

def error_message_details(error_message,error_details):
        file_name=error_details.tb_frame.f_code.co_filename
        line_num=error_details.tb_lineno
        message = "Error occured at [{0}] at Line [{1}] with error [{2}]".format(file_name,line_num,str(error_message))
        return message

class CustomException(Exception):
    def __init__(self,error_message,error_details):
        
        super().__init__(error_message)
        error_details = error_message_details(error_message,error_details)
        self.error_message=error_message
        self.error_details = error_details
        logger.error(self.error_details)



     
