import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = NetworkSecurityException.get_detailed_error_message(
            error_message=error_message,
            error_detail=error_detail
        )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        detailed_error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error_message)}"
        return detailed_error_message

    def __str__(self) -> str:
        return self.error_message
    
if __name__ == "__main__":
    try:
        logger.logging.info("Testing NetworkSecurityException")
        a = 1 / 0
    except Exception as e:
        ne = NetworkSecurityException(e, sys)
        print(ne)