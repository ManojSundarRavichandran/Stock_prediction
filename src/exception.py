import sys   #always have information 
from src.logger import logging 

def error_message_details(error,error_detail:sys): #error -> message we get      error_detail -> present in the sys 

    # return type of sys 
    _,_,exc_tb=error_detail.exc_info()  # which file ,line exception occured will be in exc_tb
    error_message="Error occured in pythons script name [{0}] and line number [{1} and error message[{2}]".format()
    file_name=exc_tb.tb_frame.f_code.co_filename    #abe to find the file name 
    file_lineno= exc_tb.tb.lineno

    file_name,file_lineno,str(error)
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys): #constructor
        super().__init__(error_message)#inheriting from exception 
        self.error_message=error_message_details(error_message,error_detail=error_details)  # modular programming way 
    
    def __str__(self):
        return self.error_message